from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver.exe")


@when('open bluecoding homepage')
def openHomePage(context):
    context.driver.get("https://www.bluecoding.com/")

@then('verify that the logo present on page')
def verifyLogo(context):
    status=context.driver.fcind_element_by_xpath("//img[@title='Blue Coding logo']").is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()
