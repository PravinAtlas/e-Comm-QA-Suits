Feature: Login functionality

  Scenario Outline: Login with username and password
    Given the user is on the login page
    When the user logs in with <username> and <password>
    Then the login attempt should behave as expected for user <username>

    Examples:
      | username                | password     |
      | standard_user           | secret_sauce |
      | locked_out_user         | secret_sauce |
      | problem_user            | secret_sauce |
      | performance_glitch_user | secret_sauce |
      # | error_user              | secret_sauce  |
      | visual_user             | secret_sauce |
