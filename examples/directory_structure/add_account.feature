Feature: Accounts

  Background:
    Given I launch browser
    When I open application
    And Enter a valid email and password
    And click on Enter

  Scenario: Add account
    Given I am on the Add Account Page
    When I add account with the name "Test"
    Then the account added message is displayed

  Scenario: Add Account already added
    Given I am on the Add Account Page
    When I add account with the name "Test"
    Then the message of account already added is displayed

  Scenario: List the Added Account
    Given I am on the List Account Page
    Then the added account is displayed

  Scenario: Edit the Added Account
    Given I am on the List Account Page
    When Edit account "Test"
    Then the account name is changed to "TestEdit"
    And the account edited message is displayed

  Scenario: Remove an added Account
    Given I am on the List Account Page
    When I remove an account
    Then the remove account message is displayed