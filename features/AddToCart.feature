Feature: Add to Cart functionality

  Scenario: Login, add item to cart, and validate cart contents
    Given the user is on the login page
    When the userr logs in with username standard_user and password secret_sauce
    And the user adds the product "Sauce Labs Backpack" to the cart
    And the user navigates to the cart page
    Then the cart should contain the product "Sauce Labs Backpack"
