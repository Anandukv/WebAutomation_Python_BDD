Feature:Sauce demo web application login testing with multiple users

  Background: common steps
    Given launch chrome browser
    When  open web application

  Scenario: Verify login scenarios with valid credential-1
    And user enter the username "standard_user" and password "secret_sauce"
    And click login button
    Then user must login to the home page


  Scenario: Verify login scenarios with valid credential-2
    And user enter the username "visual_user" and password "secret_sauce"
    And click login button
    Then user must login to the home page