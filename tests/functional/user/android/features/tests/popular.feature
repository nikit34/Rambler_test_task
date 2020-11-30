Feature: Check Popular page

  Scenario: Move sideways and check title
    When waiting 10 sec on POPULAR_PAGE
    And see match text "*от Вас" and PLACE_DIST on POPULAR_PAGE
    And see match text "Сеанс*" and TV_SESSION_DATA on POPULAR_PAGE
