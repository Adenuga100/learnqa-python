Feature: Dynamic Elements Practice

  Background: sign in
    Given User is on the login page
    When User click on cookies
    And user click on signin button
    And User enters "adenugaadeyemiisaac@gmail.com"
    And User enters as "Hardayemmh4$"
    And User click on login button

  Scenario: Click on Dynamic Elements the dashboard to Delayed Elements
    When User click on start practice as"Dynamic Elements"
    And User click on button as"Click to Show Delayed Element"
    Then user views delayed elements successfully

  Scenario: Click on Dynamic Elements from slide menu to delayed elements
    When User click "Dynamic Elements" on the slide menu
     And User click on button as"Click to Show Delayed Element"
    Then user views delayed elements successfully

  Scenario: Click on Dynamic Elements the dashboard to AJAX Data Loading
    When User click on start practice as"Dynamic Elements"
    And User click on button as"Load AJAX Data"
    And user scroll to each dynamic items
    Then user views last item

  Scenario: Click on Dynamic Elements from slide menu to AJAX Data Loading
    When User click "Dynamic Elements" on the slide menu
     And User click on button as"Load AJAX Data"
    And user scroll to each dynamic items
    Then user views last item