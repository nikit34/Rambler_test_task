Feature: Check Popular page

  Background: Wait open main page of app
    Given waiting 60 sec on POPULAR_PAGE

  Scenario: Move sideways and check title
    When see match text "Популярное" and FOOTER_TEXT on POPULAR_PAGE
#    And see elem length "5" "<" MOVE_TITLE on POPULAR_PAGE
    Given waiting 5 sec on POPULAR_PAGE
    And see elements on POPULAR_PAGE
      | elem               |
      | MOVE_TIME          |
      | PLACE              |
#      | PLACE_DIST         |
      | MOVE_TIME          |
      | IMAGE_POSTER       |
      | TRAILER_BTN        |
#      | TV_SESSION_DATA    |
   Then dragdrop from "80" "50" to "20" "50" on POPULAR_PAGE