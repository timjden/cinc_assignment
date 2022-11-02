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

        Scenario Outline: Add a Recipe to a Collection
        Given User is logged in as username: <username>, password: <password>
        Given A Collection with title: <title>, exists
        Given User is on the Dashboard page
        When User clicks Explore
        When User clicks a Recipe
        When User clicks kebab icon
        When User hovers on Add to collection
        Then Collection with title: <title>, is present
        When User clicks title: <title>
        When User clicks profile icon
        When User clicks Dashboard
        When User clicks Collections tab
        Then Recipe is visible in Collection
        Then Delete the Collection
        Examples:
        |username            |password           |title          |
        |technical_assignment|uhqom-duqmum-tepXe7|Test Collection|

        Scenario Outline: User can add a Collection with the same name as a deleted Collection
        Given User is logged in as username: <username>, password: <password>
        # Given User has added and deleted a Collection with title: <title>
        When User adds a Collection with title: <title>
        Then Error: <error_message>, does not appear
        Examples:
        |username            |password           |title          |error_message                                 |
        |technical_assignment|uhqom-duqmum-tepXe7|Test Collection|You already have a collection with that title.|
        