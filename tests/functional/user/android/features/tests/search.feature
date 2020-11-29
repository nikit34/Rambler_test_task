Feature: Check Onboarding page by template

#  Background:
#    Given

  Scenario: Check text by matches and buttons
    When see match text "*покажите смартфон* *проходите сразу в зал*" and MAIN_TEXT on ONBOARDING_PAGE
    And see match text "Живой билет" and TITLE_TEXT on ONBOARDING_PAGE
    And see button NEXT_BTN with "ДАЛЕЕ" text on ONBOARDING_PAGE
    And see button CLOSE_BTN with "ЗАКРЫТЬ" text on ONBOARDING_PAGE

  Scenario: Move right by tap next button
    When see button NEXT_BTN with "ДАЛЕЕ" text on ONBOARDING_PAGE
    Then tap button NEXT_BTN on ONBOARDING_PAGE

