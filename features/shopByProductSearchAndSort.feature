# Created by nissim.shewade at 4/19/2019
Feature: Shop by Product Search and Sort

    Scenario: Validate sort product by Price: Low to High

		Given launch application

        When user searches for product "Shoes"
        Then sort products with order "Price: Low to High"
        And verify products have been sorted with order "Price Ascending"


    Scenario:Validate sort product by Price: High to Low

        When user searches for product "Shoes"
        Then sort products with order "Price: High to Low"
        And verify products have been sorted with order "Price Descending"