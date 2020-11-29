from behave import given, when, then


@given('tap button {object:S} on {base:S}')
def step_impl(context, object, base):
    pass


@when('tap button {object:S} on {base:S}')
def step_impl(context, object, base):
    pass


@then('tap button {object:S} on {base:S}')
def step_impl(context, object, base):
    if base == 'ONBOARDING_PAGE':
        if object == 'NEXT_BTN':
            context.app.onboarding_page.tap_next_btn()
        elif object == 'CLOSE_BTN':
            context.app.onboarding_page.tap_close_btn()
        else:
            raise KeyError(f'{object} is not defined')
    else:
        raise KeyError(f'{base} is not defined')