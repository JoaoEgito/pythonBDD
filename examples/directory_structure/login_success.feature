Feature: Login Successfully

  Scenario: Login in the System
    Given I want to login
    When I insert the email and password
    And I click Enter
    Then I access the system
