from behave import given, when, then


@given('see button {object:S} is "{state}" state and "{ready}" ready to press')
def step_impl(context, object, state, ready):
    pass


@when('see button {object:S} is "{state}" state and "{ready}" ready to press')
def step_impl(context, object, state, ready):
    pass


@then('see button {object:S} is "{state}" state and "{ready}" ready to press')
def step_impl(context, object, state, ready):
    pass


@given('see partially matches text "{text}" and {object:S}')
def step_impl(context, text, object):
    if object == 'TITLE_TEXT':
        elem = context.app.onboarding_page.verify_title_text(text)
    elif object == 'MAIN_TEXT':
        pass
    else:
        raise KeyError('<object> is not defined')


@when('see partially matches text "{text}" and {object:S}')
def step_impl(context, text, object):
    pass


@then('see partially matches text "{text}" and {object:S}')
def step_impl(context, text, object):
    pass


@given('see completely matches text "{text}" and {object:S}')
def step_impl(context, text, object):
    pass


@when('see completely matches text "{text}" and {object:S}')
def step_impl(context, text, object):
    pass


@then('see completely matches text "{text}" and {object:S}')
def step_impl(context, text, object):
    pass


@given('see button {object:S} with "{text}" text')
def step_impl(context, object, text):
    pass


@when('see button {object:S} with "{text}" text')
def step_impl(context, object, text):
    pass


@then('see button {object:S} with "{text}" text')
def step_impl(context, object, text):
    pass


@given('see button {object:S} is "{ready}" ready to press')
def step_impl(context, object, ready):
    pass


@when('see button {object:S} is "{ready}" ready to press')
def step_impl(context, object, ready):
    pass


@then('see button {object:S} is "{ready}" ready to press')
def step_impl(context, object, ready):
    pass


@given('see button {object:S} is "{state}" state')
def step_impl(context, object, state):
    pass


@when('see button {object:S} is "{state}" state')
def step_impl(context, object, state):
    pass


@then('see button {object:S} is "{state}" state')
def step_impl(context, object, state):
    pass




