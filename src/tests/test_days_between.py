from main import app_days_between as app


def test_days_between01():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert app.days_diff((1982, 4, 19), (1982, 4, 22)) == 3


def test_days_between02():
    assert app.days_diff((2014, 1, 1), (2014, 8, 27)) == 238


def test_days_between03():
    assert app.days_diff((2014, 8, 27), (2014, 1, 1)) == 238


test_days_between01()
test_days_between02()
test_days_between03()
