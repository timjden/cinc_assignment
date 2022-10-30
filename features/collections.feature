Feature: Collections
    Testing the Collections functionality
        
        Scenario Outline: Add a Collection
        Given User is logged in as username: <username>, password: <password>
        Given User is on the Dashboard page
        When User clicks Collections tab
        When User adds a new Collection
        When User enters a title: <title>
        When User clicks Save
        Then A new Collection is added
        Then Delete the Collection
        Examples:
        |username            |password           |title          |
        |technical_assignment|uhqom-duqmum-tepXe7|Test Collection|