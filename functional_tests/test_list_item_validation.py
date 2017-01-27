from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
from unittest import skip
import time


class ItemValidationTest(FunctionalTest):


    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidently tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        time.sleep(1)

        # The home pag refreshes, and there is an error message saying
        # that list items cannot be empty
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now woks
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy Milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy Milk')

        # Perversly, she now decides to submit a second blank list item
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy Milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")


        # And she can correct it by filling some text in
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Make Tea')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy Milk')
        self.check_for_row_in_list_table('2: Make Tea')
