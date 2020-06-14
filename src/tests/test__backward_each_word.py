from main import app_backward_each_word as app


def test_backward_each_word01():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert app.backward_string_by_word('') == ''
    assert app.backward_string_by_word('world') == 'dlrow'


def test_backward_each_word02():
    assert app.backward_string_by_word('hello world') == 'olleh dlrow'
    assert app.backward_string_by_word('hello   world') == 'olleh   dlrow'


def test_backward_each_word03():
    assert app.backward_string_by_word('welcome to a game') == 'emoclew ot a emag'


test_backward_each_word01()
test_backward_each_word02()
test_backward_each_word03()
