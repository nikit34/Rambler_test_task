from behave import given, when, then


@given('we have onboarding screen')
def step_impl(context):
    text = context.driver.find_element_by_id("ru.rambler.kassa:id/button_next")
    assert text == 'wel', '[ERROR]: text has not matches with template'
