from main import app_acceptable_password_i as app


def test_acceptable_password_i01():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert app.is_acceptable_password('short') == False


def test_acceptable_password_i02():
    assert app.is_acceptable_password('muchlonger') == True


def test_acceptable_password_i03():
    assert app.is_acceptable_password('ashort') == False


test_acceptable_password_i01()
test_acceptable_password_i02()
test_acceptable_password_i03()
