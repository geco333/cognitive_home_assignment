import logging
import uuid

from playwright.sync_api import sync_playwright

from page_models.models import EbayHome


def test_ebay():
    search_term = "laptop"
    minimum_results = 10

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
        ebay_home.search_for_laptop(search_term)

        logging.info("Validating search results visible ...")
        ebay_home.validate_search_results_visible()

        logging.info("Validating minimum search results count ...")
        ebay_home.assert_results_count(minimum_results)

        logging.info(f"Validating at least {minimum_results} search results contain the word: 'laptop' ...")
        ebay_home.validate_search_results_contain_search_term(search_term, minimum_results)
