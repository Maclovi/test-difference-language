from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located as is_visible,
)
from selenium.webdriver.support.ui import WebDriverWait as Wait


def test_has_button(browser: WebDriver) -> None:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    timeout = 30
    button_element = Wait(browser, timeout).until(
        is_visible((By.CSS_SELECTOR, "button.btn-primary"))
    )

    assert button_element.is_enabled(), "Element is not found"
