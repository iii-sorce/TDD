from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    """
    listの要素がすべて等しいかチェック

    Parameters
    ----------
    elements : Any
        任意の値が入ったリスト

    Returns
    -------
    result : bool
    """
    # listが空か要素が１の場合はTrueを返す。
    if elements == []:
        result = True
    elif len(elements) == 1:
        result = True
    else:
        # それ以外はチェックを入れる
        result = all(elements[0] == elem for elem in elements)

    return result

"""
ex:

この記述だけで問題なく通った。
result = all(elements[0] == elem for elem in elements)
"""

