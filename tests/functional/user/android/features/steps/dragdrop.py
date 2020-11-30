from behave import then


@then('dragdrop from "{px1}" "{py1}" to "{px2}" "{py2}" on {base:S}')
def step_impl(context, px1, py1, px2, py2, base):
    if base == 'POPULAR_PAGE':
        context.app.popular_page.act.dragdrop(px1, py1, px2, py2)
    else:
        raise KeyError(f'{base} is not defined')