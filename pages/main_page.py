import allure
from base_object.base import BaseObject
from base_object.locators import MainPageLocators
from support.assertion import Assertion


class MainPage(BaseObject, Assertion):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def buy_goods(self,first_name,last_name,postal_code):
        self.click_to_add_to_cart()
        self.click_to_cart()
        self.click_to_checkout_btn()
        self.enter_information(first_name= first_name, last_name= last_name, zip_code=postal_code)
        self.click_to_continue_btn()
        self.click_to_finish_btn()

    def not_buy_goods(self,first_name,last_name,postal_code):
        self.click_to_add_to_cart()
        self.click_to_cart()
        self.click_to_checkout_btn()
        self.enter_information(first_name= first_name, last_name= last_name, zip_code=postal_code)
        self.click_to_continue_btn()

    def click_to_add_to_cart(self):
        self.click(MainPageLocators.ADD_TO_CART_BTN)

    def click_to_cart(self):
        self.click(MainPageLocators.SHOPPING_CART_BTN)

    def click_to_checkout_btn(self):
        self.click(MainPageLocators.CHECKOUT_BTN)

    def enter_information(self, first_name, last_name, zip_code):
        self.enter_text(MainPageLocators.FIRST_NAME_FIELD, first_name)
        self.enter_text(MainPageLocators.LAST_NAME_FIELD, last_name)
        self.enter_text(MainPageLocators.ZIP_FIELD, zip_code)

    def click_to_continue_btn(self):
        self.click(MainPageLocators.CONTINUE_BTN)

    def click_to_finish_btn(self):
        self.click(MainPageLocators.FINISH_BTN)

    def click_to_back_home_btn(self):
        self.click(MainPageLocators.BACK_HOME_BTN)

    def verify_title_text(self):
        self.assert_equal("Thank you for your order!", self.get_text(MainPageLocators.CHECKOUT_COMPLETE_TEXT))

    def verify_title_text_unsuccessful_buy_goods(self,expected_result):
        self.assert_equal(f"{expected_result}", self.get_text(MainPageLocators.ERROR_TEXT))
        