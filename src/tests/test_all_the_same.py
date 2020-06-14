from main import app_all_the_same as app


def test_all_the_same01():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert app.all_the_same([1, 1, 1]) == True
    assert app.all_the_same([1, 2, 1]) == False


def test_all_the_same02():
    assert app.all_the_same(['a', 'a', 'a']) == True
    assert app.all_the_same([]) == True


def test_all_the_same03():
    assert app.all_the_same([1]) == True


test_all_the_same01()
test_all_the_same02()
test_all_the_same03()
