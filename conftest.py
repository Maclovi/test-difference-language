import logging
from collections.abc import Generator
from typing import cast

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def browser(driver: WebDriver) -> Generator[WebDriver, None, None]:
    logging.info("start browser for test..\n")

    yield driver

    logging.info("\nquit browser..")
    driver.quit()


@pytest.fixture(scope="session")
def driver(language: str) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": language}
    )
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    return driver


@pytest.fixture(scope="session")
def language(request: pytest.FixtureRequest) -> str:
    opt = request.config.getoption("--language")
    return cast(str, opt)


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--language",
        action="store",
        default="es",
        help="Select the language you want to test",
    )
