Feature: Check Onboarding page by template

  Scenario: Matching text
    Given we have onboarding screen
    When we see text "eeee"
    And we see text "bbb"
    And we see button "Back"
    And we see button "Next"
    Then we tap "Next" button