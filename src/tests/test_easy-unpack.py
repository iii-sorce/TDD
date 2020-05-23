from main import app_unpack as es


def test_easy_unpack_01():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert es.easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)


def test_easy_unpack_02():
    assert es.easy_unpack((1, 1, 1, 1)) == (1, 1, 1)


def test_easy_unpack_03():
    assert es.easy_unpack((6, 3, 7)) == (6, 7, 3)


test_easy_unpack_01()
test_easy_unpack_02()
test_easy_unpack_03()
