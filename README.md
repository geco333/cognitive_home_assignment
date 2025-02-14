[![Generic badge](https://img.shields.io/badge/python-3.12-g.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/pytest-8.2.2-g.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/playwright-1.45.0-g.svg)](https://shields.io/)

# Cognitive home assignment

# Table of content

- [Installation](#Installation)
- [Usage](#Usage)

## Installation

Set up a local virtual environment using Pycharm settings or manually using the following command:

```python3 -m venv .venv```

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

> For example in order to run the test using ***laptop*** as the search term and validate ***10*** returned results use
> the following command:
>
>```pytest tests/test_ebay.py --search-term laptop --minimum-results 10```

## Logging

For each test run a new folder containing the ***debug.log*** and the HTML report file will be created in ***log/***  

The test run logging folder is named randomly using a UUID4 hash.

> For example, for test run 43086d5e-6b6d-45f5-9777-626d7af8a47c the logging files
> will be:
>  
> log/43086d5e-6b6d-45f5-9777-626d7af8a47c/debug.log
> 
> log/43086d5e-6b6d-45f5-9777-626d7af8a47c/report.html
