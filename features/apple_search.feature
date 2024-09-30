# File: apple_search.feature
Feature: Apple Search and Cart

  Scenario Outline: Search and add product to cart
    Given I am on the Apple homepage
    When I search for the "<product>"
    Then a screenshot of the search "<product>" should be taken
    When I add the first "<product>" result to the bag
    Then I should be able to proceed to the review bag
    Then a screenshot of the reviewed "<product>" should be taken
    Then the "<product>" should be removed or deleted from the bag
    Then I return to the Apple homepage

    Examples:
      | product     |
      | iPhone 16 Pro |
      | MacBook Pro |

  Scenario: Close the browser
    Then I close the browser
