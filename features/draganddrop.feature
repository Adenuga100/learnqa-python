Feature: Drag and drop

  Background: sign in
    Given User is on the login page
    When User click on cookies
    And user click on signin button
    And User enters "adenugaadeyemiisaac@gmail.com"
    And User enters as "Hardayemmh4$"
    And User click on login button

  Scenario: Click on drag and drop from the dashboard
    When User click on start practice as"Drag & Drop"
    And user drag and drop all the items
    Then user drop all the items successfully

  Scenario: Click on drag and drop from slide menu
    When User click "Drag & Drop" on the slide menu
    And user drag and drop all the items
    Then user drop all the items successfully