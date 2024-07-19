[![Generic badge](https://img.shields.io/badge/python-3.12-g.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/pytest-8.2.2-g.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/playwright-1.45.0-g.svg)](https://shields.io/)

# cognitive_home_assignment

## Installation

In order to install all dependencies run the following commands:

```
pip install -r requirenments.txt
playwright install
``` 

## Usage

The test is parameterized:
- **search-term**: The search term to input in the Ebay.com search bar.
- **minimum-results**: The minimum number of search results to validate.

In order to run the test run the following command:

``
pytest tests/test_ebay.py --search-term <search_term> --minimum-results <minimum_results>
``

> For example in order to run the test using ***laptop*** as the search term and validate ***10*** returned results use the following command:
> 
>```pytest tests/test_ebay.py --search-term laptop --minimum-results 10```