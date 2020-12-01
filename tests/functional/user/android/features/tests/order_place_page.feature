Feature: Check Order Page for choice places

  Background: Wait open main page of app
    Given waiting 50 sec on ORDER_PLACE_PAGE

  @order_place
  Scenario: Pass in order page for choice place and check elements at exists
    When tap button MOVE_TIME on POPULAR_PAGE
    Then see match text "ДАЛЕЕ" and NEXT_BTN on ORDER_PLACE_PAGE
    When see elements on ORDER_PLACE_PAGE
      | elem                 |
      | TICKET_COUNT_ONE     |
      | TICKET_COUNT_PLUS    |
      | LEVEL_MAP_VIEW       |
      | SESSION_SUB_TITLE    |
      | SESSION_TITLE        |
      | TOOLBAR              |