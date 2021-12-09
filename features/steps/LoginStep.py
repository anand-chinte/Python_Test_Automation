from behave import given
from selenium import webdriver
from Base.pages.LoginPage import LoginPage
import time


@given('User Launch browser')
def step_impl(context):
    browser = webdriver.Chrome(executable_path=r'Base/driver/chromedriver')
    browser.get('https://www.saucedemo.com/')
    login_page = LoginPage(browser)
    login_page.get_username().send_keys("standard_user")
    login_page.get_password().send_keys("secret_sauce")
    time.sleep(10)
    login_page.get_sign_in_button().click()
    browser.close()
