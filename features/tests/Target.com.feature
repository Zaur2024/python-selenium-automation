"""

Feature: Test for Card

  Scenario: User can check the card

    Given open target main page
    When click card icon
    Then Verify “Your cart is empty” message is shown


 Scenario: Verify that a logged out user can navigate to Sign In:
    Given open target main page
    When click Sign In
    And From right side navigation menu, click Sign In.
    Then Verify Sign In form opened
