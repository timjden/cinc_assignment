Feature: Recipe
    Testing Recipe

        Scenario Outline: Recipe adjustment
        Given User is logged in as username: <username>, password: <password>
        When User clicks Explore
        When User clicks a Recipe
        When User clicks adjustment icon
        When User hovers on Units
        When User clicks Metric
        When User clicks adjustment icon
        When User hovers on Scale
        When User scales recipe X2
        Then Recipe amounts have been correctly scaled
        Examples:
        |username            |password           |
        |technical_assignment|uhqom-duqmum-tepXe7|