from behave import *
from selenium import webdriver

@given('I want to login')
def launchBrowser(context):
    context.driver=webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver.exe")
    context.driver.get("https://seubarriga.wcaquino.me/login")

@when('I insert the email and password')
def insertDatas(context):
    email = context.driver.find_element_by_id("email")
    password = context.driver.find_element_by_id("senha")
    email.send_keys("a1@a1.com")
    password.send_keys("12345")

@when('I click Enter')
def clickEnterButton(context):
    context.driver.find_element_by_tag_name("button").click()

@then('I access the system')
def pageAccess(context):
    welcome = context.driver.find_element_by_xpath("//div[@class='alert alert-success']").text
    assert welcome == "Bem vindo, A!"