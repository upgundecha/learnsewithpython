Feature: I want to search for products

 Scenario Outline: Search
   Given I am on home page
   when I search for "phone"
   then I should see list of matching products in search results
