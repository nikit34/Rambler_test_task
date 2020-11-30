from base import Search


# taken from documentation https://docs.pytest.org/en/stable/example/parametrize.html
def pytest_generate_tests(metafunc):
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    metafunc.parametrize(
        argnames, [[funcargs[name] for name in argnames] for funcargs in funcarglist]
    )


class TestSearch:
    params = {
        "test_matching_text": [
            dict(data={
                'token': '*покажите смартфон* *проходите сразу в зал*',
                'pattern': 'Забудьте про очереди, покажите смартфон и проходите сразу в зал'
            }, answer=[
                'покажите смартфон',
                'проходите сразу в зал'
            ]),
            dict(data={
                'token': '*invalid text* *err...',
                'pattern': 'Забудьте про очереди, покажите смартфон и проходите сразу в зал'
            }, answer=[

            ]),
            dict(data={
                'token': 'Живой билет',
                'pattern': 'Живой билет'
            },
                answer=True
            ),
            dict(data={
                'token': 'Мертвый',
                'pattern': 'Живой билет'
            },
                answer=False
            )
        ],
    }

    def test_matching_text(self, data, answer):
        token = data['token']
        pattern = data['pattern']
        assert Search.matching_text(token, pattern) == answer, '[ERROR] matching_text'



