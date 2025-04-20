Feature: Test for search

  Scenario: User can search for tea
    Given Open Target main page
    When Search for tea
    Then Verify search results for tea


   Scenario: “Your cart is empty” message is shown for empty cart
    Given Open Target main page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown

