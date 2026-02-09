Feature: Keysboard and Mouse Practice

  Background: sign in
    Given User is on the login page
    When User click on cookies
    And user click on signin button
    And User enters "adenugaadeyemiisaac@gmail.com"
    And User enters as "Hardayemmh4$"
    And User click on login button

  Scenario: Click on Keyboard & Mouse
    When User click on start practice as"Keyboard & Mouse"
    And User click on button as"Start Scenario: Use Backspace to clear field"
    And user clear the field
    And User click on button as"Start Scenario: Click to open dialog"
    And user click on enter and esc
    And user double click
    And user mouse hover
    Then user views Keyboard & Mouse successfully

  Scenario: Click on Keyboard & Mouse slide menu
    When User click "Keyboard & Mouse Events" on the slide menu
    And User click on button as"Start Scenario: Use Backspace to clear field"
    And user clear the field
    And User click on button as"Start Scenario: Click to open dialog"
    And user click on enter and esc
    And user double click
    And user mouse hover
    Then user views Keyboard & Mouse successfully