# Created by nissim.shewade at 4/19/2019
Feature: Shop by Product Search

    Scenario: Validate shop by product search functionality

		Given launch application

        When user searches for product "jackets for men"
        Then filter products by filter-type "Material" and value "Leather"
        And validate elements in list view for sub-category "Leather"

        Then filter products by filter-type "Brands" and value "Alpine Swiss"
        And validate elements in list view for sub-category "Alpine Swiss"




