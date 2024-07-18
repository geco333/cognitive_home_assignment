import re

from playwright.sync_api import Page, expect


class EbayPage:
    def __init__(self, page: Page):
        self.url = "about:blank"
        self.locators = {}
        self.page = page

    def navigate_to(self):
        self.page.goto(self.url)

    def validate_page_finished_loading(self):
        self.page.wait_for_load_state()


class EbayHome(EbayPage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.url = "http://www.ebay.com"
        self.locators = {
            "search_bar": 'xpath=//*[@id="gh-ac"]',
            "search_button": '//*[@id="gh-btn"]',
            "search_results_list": '//*[@id="srp-river-results"]/ul',
            "search_results_list_items": '//*[@id="srp-river-results"]/ul/li',
        }

    def assert_search_bar_visible(self):
        """Validates that the search bar is visible."""

        expect(self.page.locator(self.locators['search_bar'])).to_be_visible()

    def search_for_laptop(self, search_term: str):
        """Input the search term in the search bar and click search."""

        self.page.locator(self.locators['search_bar']).fill(search_term)
        self.page.locator(self.locators['search_button']).click()

    def validate_search_results_visible(self):
        """Validate that a search returned results."""

        expect(self.page.locator(self.locators['search_results_list'])).to_be_visible()

    def assert_results_count(self, n: int):
        """Validate at least n search results"""

        assert self.page.locator(self.locators['search_results_list_items']).count() >= n

    def validate_search_results_contain_search_term(self,
                                                    search_term: str,
                                                    minimum_results: int):
        """Validate that the search results contain the search term.

        :param search_term: The search term to validate.
        :param minimum_results: The minimum results to assert.
        """

        search_results = self.page.locator(self.locators['search_results_list_items']).all()
        counter = 0

        for search_result in search_results[2:]:
            if re.search(search_term, search_result.text_content()):
                counter += 1

            if counter >= minimum_results:
                return

        raise AssertionError(f"found less then {minimum_results} search results containing 'laptop'")
