from selenium import webdriver


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def get_username(self):
        return self.browser.find_element_by_id("user-name")

    def get_password(self):
        return self.browser.find_element_by_id("password")

    def get_sign_in_button(self):
        return self.browser.find_element_by_id("login-button")

