from behave import given, when, then


@given('see match text "{text}" and {object:S} on {base:S}')
def step_impl(context, text, object, base):
    pass


@when('see match text "{text}" and {object:S} on {base:S}')
def step_impl(context, text, object, base):
    if base == 'ONBOARDING_PAGE':
        if object == 'TITLE_TEXT':
            context.app.onboarding_page.verify_title_text(text)
        elif object == 'MAIN_TEXT':
            context.app.onboarding_page.verify_main_text(text)
        else:
            raise KeyError(f'{object} is not defined')
    else:
        raise KeyError(f'{base} is not defined')


@then('see match text "{text}" and {object:S} on {base:S}')
def step_impl(context, text, object, base):
    pass


@given('see button {object:S} with "{text}" text on {base:S}')
def step_impl(context, object, text, base):
    pass


@when('see button {object:S} with "{text}" text on {base:S}')
def step_impl(context, object, text, base):
    if base == 'ONBOARDING_PAGE':
        if object == 'NEXT_BTN':
            context.app.onboarding_page.verify_next_btn(text)
        elif object == 'CLOSE_BTN':
            context.app.onboarding_page.verify_close_btn(text)
        else:
            raise KeyError(f'{object} is not defined')
    else:
        raise KeyError(f'{base} is not defined')


@then('see button {object:S} with "{text}" text on {base:S}')
def step_impl(context, object, text, base):
    pass







