from datetime import date


def days_diff(a, b):
    """
    日付の差を返す

    Parameters
    ----------
    a : tuple
        (年, 月, 日)
    b : tuple
        (年, 月, 日)

    Returns
    -------
    result : int
        2つの年月日の差
    """
    from_dt = date(a[0], a[1], a[2])
    to_dt = date(b[0], b[1], b[2])

    result = abs((to_dt - from_dt).days)
    return result


"""
ex:
from datetime import datetime

def days_diff(date1, date2):
    return abs((datetime(*date1)-datetime(*date2)).days)

"""

