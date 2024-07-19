import logging
import os
import pathlib
import uuid

import pytest

# Setup logging to a local file named using a random uuid4 hash.
root_logger = logging.getLogger()

log_folder = pathlib.Path(f"{pathlib.Path(__file__).parent}/log")

if not log_folder.exists():
    os.mkdir(log_folder)

file_handler = logging.FileHandler(f"{log_folder}/{uuid.uuid4()}.log", encoding="utf-8")
file_handler_formatter = logging.Formatter("[%(asctime)s%(msecs)d][%(levelname)s] %(message)s")
file_handler_formatter.default_msec_format = '%s.%03d'
file_handler.setFormatter(file_handler_formatter)

root_logger.addHandler(file_handler)


def pytest_addoption(parser):
    parser.addoption("--help", action="store")
    parser.addoption("--search-term", action="store")
    parser.addoption("--minimum-results", action="store")


@pytest.fixture(scope='session')
def search_term(request) -> str:
    """Command line option: the search result to input in the search bar."""

    search_term = request.config.option.search_term

    if search_term is None:
        logging.error("Must provide a search term, for example: --search-term 'laptop'")
        pytest.skip()

    return search_term


@pytest.fixture(scope='session')
def minimum_results(request) -> int:
    """Command line option: the minimum number of returned results to validate."""

    minimum_results = request.config.option.minimum_results

    if minimum_results is None:
        logging.info("Minimum number of test results was not provided, uses 10")

        return 10

    return int(minimum_results)
