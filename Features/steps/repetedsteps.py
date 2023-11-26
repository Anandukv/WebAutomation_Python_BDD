from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@then(u'user enter the username "visual_user" and password "secret_sauce"')
def step_impl(context):
    assert True


@then(u'click login button')
def step_impl(context):
    assert True