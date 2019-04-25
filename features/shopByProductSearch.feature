# Created by nissim.shewade at 4/19/2019
Feature: Shop by Product Search

    Scenario: Validate shop by product search functionality

		Given launch application

        When user searches for product "Shoes"
        Then validate elements in list view for sub-category "Shoes"

        When user searches for product "Shirts"
        Then validate elements in list view for sub-category "Shirt"

        When user searches for product "Jerseys"
        Then validate elements in list view for sub-category "Jersey"


    Scenario: Validate no products found functionality

		Given launch application

        When user searches for product "ctyrfhgjfh"
        Then validate no products found message for "ctyrfhgjfh"




