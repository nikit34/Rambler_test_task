from behave import when


@when('waiting {wait} sec on {base:S}')
def step_impl(context, wait, base):
    if int(wait) <= 0:
        raise ValueError('[ERROR] waiting time cannot be negative')
    if base == 'POPULAR_PAGE':
        context.app.popular_page.set_custom_wait(wait)
    else:
        raise KeyError(f'{base} is not defined')