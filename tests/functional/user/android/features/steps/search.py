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
    elif base == 'ORDER_PLACE_PAGE':
        if label == 'NEXT_BTN':
            context.app.order_place_page.verify_text(text, label)
    else:
        raise KeyError(f'{base} is not defined')


@when('see elem length "{length}" "{sign}" {label:S} on {base:S}')
def step_impl(context, length, sign, label, base):
    if base == 'POPULAR_PAGE':
        if label == 'MOVE_TITLE':
            context.app.popular_page.verify_length_text(length, sign, label)
        else:
            raise KeyError(f'{label} is not defined')
    else:
        raise KeyError(f'{base} is not defined')


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


@when('see elements on {base:S}')
def step_impl(context, base):
    if base == 'POPULAR_PAGE':
        for label in context.table:
            if label['elem'] in ['MOVE_TIME',
                                 'PLACE',
                                 'PLACE_DIST',
                                 'MOVE_TIME',
                                 'IMAGE_POSTER',
                                 'TRAILER_BTN',
                                 'TV_SESSION_DATA']:
                context.app.popular_page.exist_elem(label['elem'])
                break
            else:
                raise KeyError(f'{label["elem"]} is not defined')
    if base == 'ORDER_PLACE_PAGE':
        for label in context.table:
            if label['elem'] in ['TICKET_COUNT_ONE',
                                 'TICKET_COUNT_PLUS',
                                 'LEVEL_MAP_VIEW',
                                 'SESSION_SUB_TITLE',
                                 'SESSION_TITLE',
                                 'TOOLBAR']:
                context.app.popular_page.exist_elem(label['elem'])
                break
            else:
                raise KeyError(f'{label["elem"]} is not defined')
    else:
        raise KeyError(f'{base} is not defined')


@then('dont see error on {base:S}')
def step_impl(context, base):
    if base == 'ERRORS_PAGES':
        for label in context.table:
            if label['elem'] in ['TEXT_ERROR',
                                 'RETRY_BTN',
                                 'TOOLBAR']:
                context.app.errors_pages.not_exist_elem(label['elem'])
                break
            else:
                raise KeyError(f'{label["elem"]} is not defined')
    else:
        raise KeyError(f'{base} is not defined')
