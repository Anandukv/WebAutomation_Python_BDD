from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def step_launch_browser(context):
    context.driver = webdriver.Chrome()
    pass


@when('open web application')
def step_open_app(context):
    context.driver.get("https://www.saucedemo.com/")


@when('user enter the username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
    context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)


@when('click login button')
def step_click_loginbtn(context):
    context.driver.find_element(By.XPATH, "//input[@id='login-button']").click()


@then('user must login to the home page')
def step_verify_login(context):
    try:
        status = context.driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
    except Exception:
        context.driver.close()
        status = False
    if status:
        assert status is True
        context.driver.close()

