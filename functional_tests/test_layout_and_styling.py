from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class LayoutAndStylingTes(FunctionalTest):

    def test_layout_and_styling(self):
        # Edith goes to the home page_text
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # She starts a new list and sees the inputbox is nicely centered there too
        inputbox.send_keys('testing\n')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(1)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
