Feature: Check Onboarding page by template

  Background: Wait open main page of app
    Given waiting 5 sec on ONBOARDING_PAGE

  @onboarding
  Scenario: Check text by matches, tap next check text by matches and tap close
    When see match text "Живой билет" and TITLE_TEXT on ONBOARDING_PAGE
    And see match text "*покажите смартфон* *проходите сразу в зал*" and MAIN_TEXT on ONBOARDING_PAGE
    And see button NEXT_BTN with "ДАЛЕЕ" text on ONBOARDING_PAGE
    And see button CLOSE_BTN with "ЗАКРЫТЬ" text on ONBOARDING_PAGE
    Then tap button NEXT_BTN on ONBOARDING_PAGE
    When see match text "*Мы расскажем*" and MAIN_TEXT on ONBOARDING_PAGE
    And see match text "Включите геолокацию и уведомления" and TITLE_TEXT on ONBOARDING_PAGE
    And see button NEXT_BTN with "ДАЛЕЕ" text on ONBOARDING_PAGE
    And see button CLOSE_BTN with "ЗАКРЫТЬ" text on ONBOARDING_PAGE
    Then tap button CLOSE_BTN on ONBOARDING_PAGE

  @onboarding
  Scenario: Check text by matches and tap next repeat three times
    Then tap button NEXT_BTN on ONBOARDING_PAGE
    And tap button NEXT_BTN on ONBOARDING_PAGE
    When see match text "*Сохраните банковскую карту*" and MAIN_TEXT on ONBOARDING_PAGE
    And see match text "Оплата в один клик" and TITLE_TEXT on ONBOARDING_PAGE
    And see button NEXT_BTN with "НАЧАТЬ" text on ONBOARDING_PAGE
    And see button CLOSE_BTN with "ЗАКРЫТЬ" text on ONBOARDING_PAGE
    Then tap button NEXT_BTN on ONBOARDING_PAGE
