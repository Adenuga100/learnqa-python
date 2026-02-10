Feature: Shadow Dom Practice

  Background: sign in
    Given User is on the login page
    When User click on cookies
    And user click on signin button
    And User enters "adenugaadeyemiisaac@gmail.com"
    And User enters as "Hardayemmh4$"
    And User click on login button

  Scenario: Click on Shadow Dom
    When User click on start practice as"Shadow DOM"
    And User click on button as"Create Basic Shadow DOM"
    And User click on button as"Shadow Button"
    Then user views shadow successfully

  Scenario: Click on Shadow Dom slide menu
    When User click "Shadow DOM" on the slide menu
    And User click on button as"Create Basic Shadow DOM"
    And User click on button as"Shadow Button"
    Then user views shadow successfully