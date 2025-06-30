Feature: Cart Validation

  Scenario: Login, add multiple items to cart, and validate cart contents
    Given the user is on the login page
    When the userrr logs in with standard_user and secret_sauce
    And the user adds the following products to the cart
      | products                |
      | Sauce Labs Backpack     |
      | Sauce Labs Bike Light   |
      | Sauce Labs Bolt T-Shirt |
    And the user navigates to the cart page
    Then the cart should contain the following products
      | products                |
      | Sauce Labs Backpack     |
      | Sauce Labs Bike Light   |
      | Sauce Labs Bolt T-Shirt |
