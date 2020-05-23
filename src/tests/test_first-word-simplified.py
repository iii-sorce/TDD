from main import app_first_word_simplified as app


def test_first_word_simplified_01():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert app.first_word("Hello world") == "Hello"


def test_first_word_simplified_02():
    assert app.first_word("a word") == "a"


def test_first_word_simplified_03():
    assert app.first_word("hi") == "hi"


test_first_word_simplified_01()
test_first_word_simplified_02()
test_first_word_simplified_03()
