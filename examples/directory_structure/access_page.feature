
  Feature: Login Users

    Background:
      Given I launch the Swaglabs browser
      When I access the Swaglabs page
      Then the Login page is displayed

    Scenario: Access with Standard User
      Given I am on Swaglabs page
      When I insert the username standard_user
      And I insert the password
      And I click Login
      Then The Product Page is displayed

    Scenario: Access with Lock Out User
      Given I am on Swaglabs page
      When I insert the username locked_out_user
      And I insert the password
      And I click Login
      Then The Lockout Message is displayed

    Scenario: Access with Problem User
      Given I am on Swaglabs page
      When I insert the username problem_user
      And I insert the password
      And I click Login
      Then The Problem Page is displayed

    Scenario: Access with Perfomance Glitch User
      Given I am on Swaglabs page
      When I Access Perfomance page
      Then Perfomance Page is displayed

