from selenium.webdriver.common.by import By


class Locators:
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    TITLE_TEXT = (By.CLASS_NAME, "title")
    MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_BTN = (By.ID, "logout_sidebar_link")
    ERROR_TEXT = (By.XPATH, "//h3[@data-test='error']")
    LOGOUT_TEXT = (By.CLASS_NAME, "login_logo")



