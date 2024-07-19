import logging

from playwright.sync_api import sync_playwright

from page_models.models import EbayHome


def test_ebay(search_term: str, minimum_results: int):
    """Test steps:
    1. Open a new Chrome browser and navigate to Ebay.com
    2. Validate that the page finished loading successfully.
    3. Assert that the search bar is visible.
    4. Input the provided <search_term> into the search bar and click the search button.
    5. Validate that the search returned results.
    6. Validate that at least <minimum_results> results returned.
    7. Validate that the search returned at least <minimum_results> results containing the <search_term>"""

    logging.debug(f"search_term: {search_term}")
    logging.debug(f"minimum_results: {minimum_results}")

    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch(headless=False)
        page = browser.new_page()

        ebay_home = EbayHome(page)

        logging.info("Navigating to Ebay.com ...")
        ebay_home.navigate_to()

        logging.info("Waiting for page to finish loading ...")
        ebay_home.validate_page_finished_loading()

        logging.info("Validating search bar visible ...")
        ebay_home.assert_search_bar_visible()

        logging.info(f"Searching for {search_term} ...")
        ebay_home.search_for_search_term(search_term)

        logging.info("Validating search results visible ...")
        ebay_home.validate_search_results_visible()

        logging.info("Validating minimum search results count ...")
        ebay_home.assert_results_count(minimum_results)

        logging.info(f"Validating at least {minimum_results} search results contain the word: 'laptop' ...")
        ebay_home.validate_search_results_contain_search_term(search_term, minimum_results)
