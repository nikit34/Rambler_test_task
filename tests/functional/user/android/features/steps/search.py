from behave import given, when, then


@when('see match text "{text}" and {label:S} on {base:S}')
@then('see match text "{text}" and {label:S} on {base:S}')
def step_impl(context, text, label, base):
    if base == 'ONBOARDING_PAGE':
        if label == 'TITLE_TEXT':
            context.app.onboarding_page.verify_text(text, label)
        elif label == 'MAIN_TEXT':
            context.app.onboarding_page.verify_text(text, label)
        else:
            raise KeyError(f'{label} is not defined')
    elif base == 'POPULAR_PAGE':
        if label == 'FOOTER_TEXT':
            context.app.popular_page.verify_text(text, label)
        else:
            raise KeyError(f'{label} is not defined')
    else:
        raise KeyError(f'{base} is not defined')


@when('see elem have length "{length}" "{sign}" {label:S} on {base:S}')
def step_impl(context, length, sign, label, base):
    if base == 'ONBOARDING_PAGE':
        if label == 'TITLE_TEXT':
            pass
        elif label == 'MAIN_TEXT':
            pass
        else:
            raise KeyError(f'{label} is not defined')
    elif base == 'POPULAR_PAGE':
        if label == 'MOVE_TITLE':
            context.app.popular_page.verify_length_text(length, sign, label)
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




