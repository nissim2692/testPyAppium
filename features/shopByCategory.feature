# Created by nissim.shewade at 4/19/2019
Feature: Shop by Category
	Scenario: Configure and launch Appium

		Given launch application
        Then user clicks on Shop by Category
        Then validate elements in list view for Shop By Category
        Then user selects "Men's Fashion" category
        Then user selects "Amazon Fashion" option in category view
        Then user clicks on "Casuals and Denims " sub-category
        Then user clicks on element with description "Skinny" from result set
        And validate elements in list view for sub-category "Jeans"