from main import app_first_word as app


def test_first_word01():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert app.first_word("Hello world") == "Hello"
    assert app.first_word(" a word ") == "a"


def test_first_word02():
    assert app.first_word("don't touch it") == "don't"
    assert app.first_word("greetings, friends") == "greetings"


## TODO ... and so on ... error
def test_first_word03():
    assert app.first_word("... and so on ...") == "and"
    assert app.first_word("hi") == "hi"
    assert app.first_word("Hello.World") == "Hello"


test_first_word01()
test_first_word02()
test_first_word03()
