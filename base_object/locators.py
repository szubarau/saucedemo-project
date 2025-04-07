from selenium.webdriver.common.by import By


class IndexPageLocators:
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    TITLE_TEXT = (By.CLASS_NAME, "title")
    MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")
    LOGOUT_TEXT = (By.CLASS_NAME, "login_logo")
    ERROR_TEXT = (By.CSS_SELECTOR, "h3[data-test='error']")


class MainPageLocators:

    LOGOUT_BTN = (By.ID, "logout_sidebar_link")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_BTN = (By.ID, "shopping_cart_container")
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ZIP_FIELD = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CHECKOUT_COMPLETE_TEXT = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BTN = (By.ID, "back-to-products")
    ERROR_TEXT = (By.CSS_SELECTOR, "h3[data-test='error']")
