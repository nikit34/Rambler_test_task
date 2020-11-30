from behave import given, when


@when('see match text "{text}" and {label:S} on {base:S}')
def step_impl(context, text, label, base):
    if base == 'ONBOARDING_PAGE':
        if label == 'TITLE_TEXT':
            context.app.onboarding_page.verify_text(text, label)
        elif label == 'MAIN_TEXT':
            context.app.onboarding_page.verify_text(text, label)
        else:
            raise KeyError(f'{label} is not defined')
    else:
        raise KeyError(f'{base} is not defined')


@given('see button {label:S} with "{text}" text on {base:S}')
@when('see button {label:S} with "{text}" text on {base:S}')
def step_impl(context, label, text, base):
    if base == 'ONBOARDING_PAGE':
        if label == 'NEXT_BTN':
            context.app.onboarding_page.verify_text(text, label)
        elif label == 'CLOSE_BTN':
            context.app.onboarding_page.verify_text(text, label)
        else:
            raise KeyError(f'{label} is not defined')
    else:
        raise KeyError(f'{base} is not defined')




