from behave import then


@then('move {label:S} from "{elem1}" to "{elem2}" on {base:S}')
def step_impl(context, label, elem1, elem2, base):
    if base == 'POPULAR_PAGE':
        context.app.popular_page.act.move_obj_from_elem_to_elem(label, elem1, elem2)
    else:
        raise KeyError(f'{base} is not defined')



