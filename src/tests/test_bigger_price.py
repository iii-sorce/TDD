from main import app_bigger_price as app


def test_bigger_price01():
    # These "asserts" are used for self-checking and not for an auto-testing
    assert app.bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"


def test_bigger_price02():
    assert app.bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"


def test_bigger_price03():
    pass


test_bigger_price01()
test_bigger_price02()
test_bigger_price03()
