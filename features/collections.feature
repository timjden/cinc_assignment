Feature: Collections
    Testing the Collections functionality
        
        Scenario Outline: Add a Collection
        Given User is logged in as username: <username>, password: <password>
        Given User is on the Dashboard page
        When User clicks Collections tab
        When User adds a new Collection
        Then A new Collection is added
        Examples:
        |username            |password           |
        |technical_assignment|uhqom-duqmum-tepXe7|