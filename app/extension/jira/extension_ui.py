import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action")
    def measure():

        @print_timing("selenium_app_custom_action:view_issue_figma_designs")
        def sub_measure():
            page.wait_until_visible((By.CSS_SELECTOR, "iframe[data-ac-polyfill]"))  # Wait for you app-specific UI element by ID selector
        sub_measure()
    measure()
