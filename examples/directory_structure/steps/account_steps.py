from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


ALERT_MSG = "//div[@role='alert']"

@given('I launch browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\ChromeDriver\chromedriver.exe")

@when('I open application')
def accessPage(context):
    context.driver.get("https://seubarriga.wcaquino.me/login")


@when('Enter a valid email and password')
def insertEmailPassword(context):
    email = context.driver.find_element_by_id("email")
    password = context.driver.find_element_by_id("senha")
    email.send_keys("a1@a1.com")
    password.send_keys("12345")


@when('click on Enter')
def clickEnterButton(context):
    context.driver.find_element_by_tag_name("button").click()

@given('I am on the Add Account Page')
def add_account_page(context):
    context.driver.find_element(by=By.LINK_TEXT, value="Contas").click()
    context.driver.find_element(by=By.LINK_TEXT, value="Adicionar").click()
    assert True, context.driver.find_element(by=By.ID, value="nome")

@when('I add account with the name {accountName}')
def add_account(context, accountName):
    nome = context.driver.find_element(by=By.ID, value="nome")
    nome.send_keys(accountName)
    context.driver.find_element(by=By.TAG_NAME, value="button").click()

@then('the account added message is displayed')
def add_account_message(context):
    addAccount = context.driver.find_element_by_xpath(ALERT_MSG).text
    assert addAccount == "Conta adicionada com sucesso!"


@then('the message of account already added is displayed')
def added_account_message(context):
    addedAccount = context.driver.find_element_by_xpath(ALERT_MSG).text
    assert addedAccount == "Já existe uma conta com esse nome!"

@given('I am on the List Account Page')
def list_account_page(context):
    context.driver.find_element(by=By.LINK_TEXT, value="Contas").click()
    context.driver.find_element(by=By.LINK_TEXT, value="Listar").click()


@then('the added account is displayed')
def account_list(context):
    listedAccount = context.driver.find_element_by_xpath(
        "//td[normalize-space()='Test']").text
    assert listedAccount == "Test"

@when('Edit account {accountName}')
def edit_account(context, accountName):
    X = 1

    while (context.driver.find_element_by_xpath(
            "/html[1]/body[1]/table[1]/tbody[1]/tr["+ str(X) +"]/td[1]").text) != accountName:
        X = X + 1
    context.driver.find_element_by_xpath(
        "/html[1]/body[1]/table[1]/tbody[1]/tr[" + str(X) + "]/td[2]/a[1]/span[1]").click()
    nome = context.driver.find_element(by=By.ID, value="nome")
    nome.send_keys("Edit")
    context.driver.find_element(by=By.TAG_NAME, value="button").click()


@then('the account name is changed to {newAccountName}')
def edited_account(context, newAccountName):
    listedAccount = context.driver.find_element_by_xpath(
        "//td[normalize-space()='TestEdit']").text
    assert listedAccount == newAccountName

@then('the account edited message is displayed')
def edited_account_message(context):
    editedAccountMsg = context.driver.find_element_by_xpath(ALERT_MSG).text
    assert editedAccountMsg == "Conta alterada com sucesso!"

@when('I remove {newAccountName} account')
def remove_account(context, newAccountName):
    X = 1
    while (context.driver.find_element_by_xpath(
            "/html[1]/body[1]/table[1]/tbody[1]/tr[" + str(X) + "]/td[1]").text) != newAccountName:
        X = X + 1
    context.driver.find_element_by_xpath(
        "/html[1]/body[1]/table[1]/tbody[1]/tr[" + str(X) + "]/td[2]/a[2]/span[1]").click()

@then('the remove account message is displayed')
def remove_account(context):
    removedAccountMsg = context.driver.find_element_by_xpath(ALERT_MSG).text
    assert removedAccountMsg == "Conta removida com sucesso!"

    try:
        delAccount = context.driver.find_element_by_xpath(
            "//td[normalize-space()='TestEdit']")
    except NoSuchElementException:
        return False
    return True

    assert delAccount != True