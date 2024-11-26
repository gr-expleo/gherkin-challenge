# In this section I will break down the problem into smaller problems:
- To begin with we have the Gherkin syntax with certain keywords: 
    - Feature
        - Scenario
            - Given
            - When
            - Then
            - And

- Our input is going to be:
Feature: Guess the word
  Scenario: Maker starts a game
    When the Maker starts a game
    Then the Maker waits for a Breaker to join

  Scenario: Breaker joins a game
    Given the Maker has started a game with the word silky
    When the Breaker joins the Maker's game
    Then the Breaker must guess a word with 5 characters

We need to receive a .txt file which has a similar input as the aforementioned scenarios. 
If it has any errors, display the errors and let the user know what's wrong.

If there are no errors, display the tree. I'll do in a JSON format as it would represent the tree in a good / understandable manner. 
For example, 1 Feature can have many scenarios , each scenario can have many steps. Which is represented in the following format: 1:N -> 1:N
Example:
`
{
    "Feature": "Guess the word",
    "Scenarios": [
        {
            "Scenario": "Maker starts a game",
            "Steps": [
                {"When": "the Maker starts a game"},
                {"Then": "the Maker waits for a Breaker to join"}
            ]
        },
        {
            "Scenario": "Breaker joins a game",
            "Steps": [
                {"Given": "the Maker has started a game with the word silky"},
                {"When": "the Breaker joins the Maker's game"},
                {"Then": "the Breaker must guess a word with 5 characters"}
            ]
        }
    ]
}`

# Edge cases:
- What we can notice is that our keywords have semicolon in places, for example Feature: / Scenario: we have to make sure that we capture them.
- Case sensitivity in the 'FEATURE', 'SCENARIO', 'GIVEN', 'WHEN', 'THEN', 'AND', 'TEXT'. I would assume that we should make sure that we are as concise as possible, but getting around case sensitivity problems as such.
- Make sure to display it in a correct manner.
- Success would be represented by 200 / Error would be represented as (400 Bad request as it is appropriate)
- Make sure we can pass multiple Features / Scenarios
- Make sure to skip comment rows.

# Further improvements
- If I were to do further improvements, I would make sure that When and Then are always provided
- The current validation is very basic, I would improve the validation and it would actually separate the features and scenarios and then iterate over each one of them, just to add granularity to the validation.