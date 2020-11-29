Feature: Check Onboarding page by template

  Background:
    Given see partially matches text "*покажите телефон* проходите сразу в зал" and MAIN_TEXT

  Scenario: Check text by matches and buttons
    When see completely matches text "Живой билет" and TITLE_TEXT
    Then see button CLOSE_BTN with "ЗАКРЫТЬ" text
    And see button NEXT_BTN with "ДАЛЕЕ" text

  Scenario: State of buttons
    When see button NEXT_BTN is "" ready to press
    Then see button NEXT_BTN is "active" state
    And see button CLOSE_BTN is "nonactive" state and "" ready to press

