Feature: Check Popular page

  Scenario: Move sideways and check title
    When waiting 10 sec on POPULAR_PAGE
    And see match text "MOVE_TITLE" and "*ИНТЕЛЛЕКТ" on POPULAR_PAGE
