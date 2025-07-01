@api
Feature: Reqres API Scenarios

  Scenario: Get a list of users on page 1
    When the client requests the list of users on page 1
    Then the response status code should be 200
    And the response should contain a user with email george.bluth@reqres.in
