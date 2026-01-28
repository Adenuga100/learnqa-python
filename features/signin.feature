Feature: User Login

  Scenario: Successful login with valid credentials
    Given User is on the login page
    When user click on signin button
    And User enters "adenugaadeyemiisaac@gmail.com"
    And User enters as "Hardayemmh4$"
    And User click on login button
    Then User should be redirected to the inventory page
