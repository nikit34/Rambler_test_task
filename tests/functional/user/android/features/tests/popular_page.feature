Feature: Check Popular page
  
  Background: Wait open main page of app
    Given waiting 60 sec on POPULAR_PAGE

    
  Scenario: Move sideways and check title
    When see match text "Популярное" and FOOTER_TEXT on POPULAR_PAGE
    And see elem length "5" "<" MOVE_TITLE on POPULAR_PAGE
    Given waiting 5 sec on POPULAR_PAGE
    When see elements on POPULAR_PAGE
      | elem               |
      | MOVE_TIME          |
      | PLACE              |
#      | PLACE_DIST         |
      | MOVE_TIME          |
      | IMAGE_POSTER       |
      | TRAILER_BTN        |
#      | TV_SESSION_DATA    |
    Then dragdrop from "90" "50" to "10" "50" on POPULAR_PAGE
    When see match text "Популярное" and FOOTER_TEXT on POPULAR_PAGE
    And see elem length "5" "<" MOVE_TITLE on POPULAR_PAGE
    Given waiting 5 sec on POPULAR_PAGE
    When see elements on POPULAR_PAGE
      | elem               |
      | MOVE_TIME          |
      | PLACE              |
#      | PLACE_DIST         |
      | MOVE_TIME          |
      | IMAGE_POSTER       |
      | TRAILER_BTN        |
#      | TV_SESSION_DATA    |
    Then dragdrop from "90" "30" to "10" "30" on POPULAR_PAGE
    And dragdrop from "10" "60" to "90" "40" on POPULAR_PAGE
  
    
  Scenario: Pass in order page for choice place
    When tap button MOVE_TIME on POPULAR_PAGE
    Then see match text "ДАЛЕЕ" and NEXT_BTN on ORDER_PLACE_PAGE