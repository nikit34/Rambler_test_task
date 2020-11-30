from behave import when


@when('waiting {timeout} sec on {base:S}')
def step_impl(context, timeout, base):
    if int(timeout) <= 0:
        raise ValueError('[ERROR] waiting time cannot be negative')
    if base == 'POPULAR_PAGE':
        context.app.popular_page.set_timeout(timeout)
    else:
        raise KeyError(f'{base} is not defined')