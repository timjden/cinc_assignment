Feature: Login
    Testing Login

        Scenario Outline: Login
        Given User is on the Home page
        When User clicks Log In
        Then Log in dialog pops up
        When User enters username: <username>
        When User enters password: <password>
        When User clicks Log in button
        Then User is logged in
        Examples:
        |username            |password           |
        |technical_assignment|uhqom-duqmum-tepXe7|