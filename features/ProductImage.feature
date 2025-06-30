Feature: Image Compare functionality

  Scenario: Compare product image with baseline
    Given the user is on the login page
    When the userr logs in with username standard_user and password secret_sauce
    And the user captures the image of Sauce Labs Backpack
    Then the product image should match the baseline for Sauce Labs Backpack
