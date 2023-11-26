
Feature:Sauce demo web application login testing with multiple users
   Scenario Outline: Verify login scenarios with multiple valid credential
     Given launch chrome browser
     When  open web application
     And user enter the username "<username>" and password "<secret_sauce>"
     And click login button
     Then user must login to the home page

     Examples:
      | username | password |
      | standard_user | secret_sauce |
      | locked_out_user | secret_sauce |
      | problem_user | secret_sauce |
      | performance_glitch_user | secret_sauce |
      | visual_user | secret_sauce |

