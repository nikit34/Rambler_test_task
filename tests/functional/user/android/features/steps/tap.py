from behave import when, then


@when('tap button {label:S} on {base:S}')
@then('tap button {label:S} on {base:S}')
def step_impl(context, label, base):
    if base == 'ONBOARDING_PAGE':
        if label == 'NEXT_BTN':
            context.app.onboarding_page.tap_btn(label)
        elif label == 'CLOSE_BTN':
            context.app.onboarding_page.tap_btn(label)
    elif base == 'POPULAR_PAGE':
        if label == 'MOVE_TIME':
            context.app.popular_page.tap_btn(label)
        else:
            raise KeyError(f'{label} is not defined')
    else:
        raise KeyError(f'{base} is not defined')