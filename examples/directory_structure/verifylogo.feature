
Feature: Google Logo


Scenario: Logo presence on Google home page

    Given launch chrome browser
    When open bluecoding homepage
    Then verify that the logo present on page
    And close browser