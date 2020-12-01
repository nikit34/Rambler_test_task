Feature: Check Order Page for choice places

  Background: Wait open main page of app
    Given waiting 5 sec on ORDER_PLACE_PAGE

  @order_place
  Scenario: Check elements at exists
    When see elements on ORDER_PLACE_PAGE
      | elem                 |
      | TICKET_COUNT_ONE     |
      | TICKET_COUNT_PLUS    |
      | LEVEL_MAP_VIEW       |
      | SESSION_SUB_TITLE    |
      | SESSION_TITLE        |
      | TOOLBAR              |