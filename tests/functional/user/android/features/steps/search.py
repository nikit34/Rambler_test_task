from behave import given, when, then


@given('see button {object:S} is "{state}" state and "{ready}" ready to press on {base:S}')
def step_impl(context, object, state, ready, base):
    pass


@when('see button {object:S} is "{state}" state and "{ready}" ready to press on {base:S}')
def step_impl(context, object, state, ready, base):
    pass


@then('see button {object:S} is "{state}" state and "{ready}" ready to press on {base:S}')
def step_impl(context, object, state, ready, base):
    pass


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
    pass


@then('see button {object:S} with "{text}" text on {base:S}')
def step_impl(context, object, text, base):
    if base == 'ONBOARDING_PAGE':
        if object == 'NEXT_BTN':
            pass
        elif object == 'CLOSE_BTN':
            pass
        else:
            raise KeyError(f'{object} is not defined')
    else:
        raise KeyError(f'{base} is not defined')


@given('see button {object:S} is "{ready}" ready to press on {base:S}')
def step_impl(context, object, ready, base):
    pass


@when('see button {object:S} is "{ready}" ready to press on {base:S}')
def step_impl(context, object, ready, base):
    pass


@then('see button {object:S} is "{ready}" ready to press on {base:S}')
def step_impl(context, object, ready, base):
    pass


@given('see button {object:S} is "{state}" state on {base:S}')
def step_impl(context, object, state, base):
    pass


@when('see button {object:S} is "{state}" state on {base:S}')
def step_impl(context, object, state, base):
    pass


@then('see button {object:S} is "{state}" state on {base:S}')
def step_impl(context, object, state, base):
    pass




