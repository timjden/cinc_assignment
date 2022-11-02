# Revio Technical Assignment

I've used an existing recipe website [cinc.kitchen] to build a few automated UI tests that roughly cover the theme of the assignment.
When you merge into `main` via PR then the tests are automatically executed and the link to the report is published on the PR. I have also attached some gifs for demonstration. I actually uncovered a bug during this exercise... a user cannot add a new collection that has the same name as a deleted collection. So the test I wrote for this will fail.

## Execution of UI Tests
![](https://github.com/timjden/cinc_assignment/blob/main/gifs/automated_tests.gif)

## Tests Executed Automatically on PR
![](https://github.com/timjden/cinc_assignment/blob/main/gifs/action.gif)

## Allure Report from PR
![](https://github.com/timjden/cinc_assignment/blob/main/gifs/allure_from_pr.gif)
