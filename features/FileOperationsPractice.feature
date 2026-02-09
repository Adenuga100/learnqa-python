Feature: File Operations Practice

  Background: sign in
    Given User is on the login page
    When User click on cookies
    And user click on signin button
    And User enters "adenugaadeyemiisaac@gmail.com"
    And User enters as "Hardayemmh4$"
    And User click on login button

  Scenario: Click on File Operations
    When User click on start practice as"File Operations"
    And User click on button as"Download Template Excel"
    And user select a file
    And user click on  download button
    Then user views file processed successfully

  Scenario: Click on File Operations
    When User click "File Operations" on the slide menu
    And User click on button as"Download Template Excel"
    And user select a file
    And user click on  download button
    Then user views file processed successfully