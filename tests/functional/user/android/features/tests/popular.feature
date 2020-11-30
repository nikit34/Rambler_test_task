Feature: Check Popular page

  Background: Wait open main page of app
    Given waiting 40 sec on POPULAR_PAGE

  Scenario: Move sideways and check title
    When see match text "*от Вас" and PLACE_DIST on POPULAR_PAGE
    And see match text "Сеанс*" and TV_SESSION_DATA on POPULAR_PAGE
