import time

import pytest

from base_object.base import BaseObject
from base_object.locators import Locators
from support.assertion import Assertion




class IndexPage(BaseObject, Assertion):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self,user_name,password):
        self.enter_user_name(text=user_name)
        self.enter_password(text=password)
        self.click_to_login_btn()

    def logout(self):
        self.click_to_menu()
        self.click_to_logout_btn()

    def enter_user_name(self, text):
        self.enter_text(Locators.USER_NAME_FIELD, text)

    def enter_password(self, text):
        self.enter_text(Locators.PASSWORD_FIELD, text)

    def click_to_login_btn(self):
        self.click(Locators.LOGIN_BTN)

    def click_to_menu(self):
        self.click(Locators.MENU)

    def click_to_logout_btn(self):
        self.click(Locators.LOGOUT_BTN)

    def verify_title_text(self):
        self.assert_equal("Products", self.get_text(Locators.TITLE_TEXT))

    def verify_title_text_logout(self):
        self.assert_equal("Swag Labs", self.get_text(Locators.LOGOUT_TEXT))

    def verify_title_text_unsuccessful_login(self,expected_result):
        self.assert_equal(f"{expected_result}", self.get_text(Locators.ERROR_TEXT))


