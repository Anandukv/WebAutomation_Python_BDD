Feature:Sauce demo web application login testing
  Scenario: Verify login scenarios with valid credential
    Given launch chrome browser
    When  open web application
    And user enter the username "standard_user" and password "secret_sauce"
    And click login button
    Then user must login to the home page