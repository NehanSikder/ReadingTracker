Feature: Reading Tracker Login
  Verify login functionality of reading tracker app

  Scenario: Successfully login with test user
    Given I navigate to localhost
    When I enter test user name and test password
    Then I should see the welcome page