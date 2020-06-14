from main import app_count_digits as app


def test_count_digits01():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert app.count_digits('hi') == 0
    assert app.count_digits('who is 1st here') == 1
    assert app.count_digits('my numbers is 2') == 1


def test_count_digits02():
    assert app.count_digits('This picture is an oil on canvas '
                        'painting by Danish artist Anna '
                        'Petersen between 1845 and 1910 year') == 8


def test_count_digits03():
    assert app.count_digits('5 plus 6 is') == 2
    assert app.count_digits('') == 0


test_count_digits01()
test_count_digits02()
test_count_digits03()
