from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@given('I launch the Swaglabs browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver.exe")

@when('I access the Swaglabs page')
def swagLoginPage(context):
    context.driver.get("https://www.saucedemo.com/")

@then('the Login page is displayed')
def loginPage(context):
    try:
        loginLogo = context.driver.find_element(by=By.CLASS_NAME, value="login_logo")
    except NoSuchElementException:
        return False
    return True
    assert loginLogo == True

@given('I am on Swaglabs page')
def loginPage(context):
    try:
        loginLogo = context.driver.find_element(by=By.CLASS_NAME, value="login_logo")
    except NoSuchElementException:
        return False
    return True
    assert loginLogo == True


@when('I insert the username {username}')
def insertUser(context, username):
    context.driver.find_element_by_id("user-name").send_keys(username)

@when('I insert the password')
def insertPassword(context):
    context.driver.find_element_by_id("password").send_keys("secret_sauce")

@when('I click Login')
def clickLoginButton(context):
    start = time.time()
    context.driver.find_element_by_id("login-button").click()
    end = time.time()
    print(end - start)

@then('The Product Page is displayed')
def productPage(context):
    l = context.driver.find_element_by_xpath("//img[@alt='Sauce Labs Backpack']")
    picture = l.get_attribute("src")
    print(picture)
    assert picture == "https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.34e7aa42.jpg"



@then('The Lockout Message is displayed')
def lockoutMsg(context):
    lockoutMessage = context.driver.find_element_by_xpath("//div[@class='error-message-container error']").text
    print(lockoutMessage)
    assert lockoutMessage == "Epic sadface: Sorry, this user has been locked out."

@then(u'The Problem Page is displayed')
def problemPage(context):
    l = context.driver.find_element_by_xpath("//img[@alt='Sauce Labs Backpack']")
    picture = l.get_attribute("src")
    print(picture)
    assert picture == "https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg"

@when(u'I Access Perfomance page')
def accessPerformancePage(context):
    context.driver.find_element_by_id("user-name").send_keys("performance_glitch_user")
    context.driver.find_element_by_id("password").send_keys("secret_sauce")

@then(u'Perfomance Page is displayed')
def performancePage(context):
    start = time.time()
    context.driver.find_element_by_id("login-button").click()
    end = time.time()
    print(end - start)
    assert end > 0.087

