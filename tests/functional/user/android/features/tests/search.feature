Feature: Check Onboarding page by template

  Background:
    Given see partially matches text "*покажите телефон* проходите сразу в зал"

  Scenario: Check text by matches and buttons
    When see completely matches text "{text}" and "Живой билет"
    Then see button "{btn}" with "ЗАКРЫТЬ" text
    And see button "{btn}" with "ДАЛЕЕ" text

  Scenario: State of buttons
    When see button "{btn}" is "" ready to press
    Then see button "{btn}" is "nonactive" state
    And see button "{btn}" is "inactive" state and "" ready to press

