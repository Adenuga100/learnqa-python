Feature: User sign up

  Scenario: Successful login with valid credentials
    Given User is on the login page
    When User click on cookies
    When user click on sign up button
    And user enters full name as"Adenuga yemi"
    And User enters "adenugaadeyem@gmail.com"
    And User enters as "Hardayemmh4$"
    And User click on create account button
    Then User should be redirected to the inventory page