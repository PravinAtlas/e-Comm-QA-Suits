@api
Feature: Reqres API Scenarios

  Scenario: Get a list of users
    When the client requests the list of users on page 2
    Then the response status code should be 200
    And the response should contain a user with email michael.lawson@reqres.in

  Scenario: Create a new user
    When the client creates a user with name morpheus and job leader
    Then the response status code should be 201
    And the response should contain the name morpheus

  Scenario: Get a single user not found
    When the client requests user with id 23
    Then the response status code should be 404
