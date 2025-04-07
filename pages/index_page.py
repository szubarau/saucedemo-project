import allure
from base_object.base import BaseObject
from base_object.locators import IndexPageLocators
from support.assertion import Assertion


class IndexPage(BaseObject, Assertion):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('log in to the app')
    def login(self, user_name, password):
        self.enter_user_name(text=user_name)
        self.enter_password(text=password)
        self.click_to_login_btn()

    @allure.step('log out to the app')
    def logout(self):
        self.click_to_menu()
        self.click_to_logout_btn()

    @allure.step('enter user name')
    def enter_user_name(self, text):
        self.enter_text(IndexPageLocators.USER_NAME_FIELD, text)

    @allure.step('enter password')
    def enter_password(self, text):
        self.enter_text(IndexPageLocators.PASSWORD_FIELD, text)

    @allure.step('click to login button')
    def click_to_login_btn(self):
        self.click(IndexPageLocators.LOGIN_BTN)

    @allure.step('click to menu')
    def click_to_menu(self):
        self.click(IndexPageLocators.MENU)

    @allure.step('click to log out button')
    def click_to_logout_btn(self):
        self.click(IndexPageLocators.LOGOUT_BTN)

    @allure.step('verify title text')
    def verify_title_text(self):
        self.assert_equal("Products", self.get_text(IndexPageLocators.TITLE_TEXT))

    @allure.step('verify title text')
    def verify_title_text_logout(self):
        self.assert_equal("Swag Labs", self.get_text(IndexPageLocators.LOGOUT_TEXT))

    @allure.step('verify title text')
    def verify_title_text_unsuccessful_login(self, expected_result):
        self.assert_equal(f"{expected_result}", self.get_text(IndexPageLocators.ERROR_TEXT))
