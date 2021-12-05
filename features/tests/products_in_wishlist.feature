# Created by Chopp at 11/29/2021
Feature: Test cases for wishlist functionality

  Scenario: Adding products to the wishlist
    Given Open GetTop homepage
    When Click on Mac in header
    And Hover over first item
    And Hover over heart icon
    And Click heart icon to add to wishlist
    Then Verify that correct item is shown in wishlist


  Scenario: Removing products from the wishlist
    Given Open GetTop homepage
    When Click on Mac in header
    And Hover over first item
    And Hover over heart icon
    And Click heart icon to add to wishlist
    And Verify that item is in wishlist
    Then Click the remove this product button
    Then Verify that product is removed from wishlist


  Scenario: Verify user sees product page by clicking item in wishlist
    Given Open GetTop homepage
    When Click on Mac in header
    And Hover over first item
    And Hover over heart icon
    And Click heart icon to add to wishlist
    And Verify that item is in wishlist
    Then Click on product in wishlist
    Then Verify user is redirected to the correct product page


  Scenario: User can see social logos to share wishlist items
    Given Open GetTop homepage
    When Click on Mac in header
    And Hover over first item
    And Hover over heart icon
    And Click heart icon to add to wishlist
    Then Verify redirect to wishlist page
    And Verify that social logos are shown on wishlist page