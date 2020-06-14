import re


def count_digits(text: str) -> int:
    """
    文字列から数字が何桁存在するかカウントする

    Parameters
    ----------
    text : str
        ランダムな文字列

    Returns
    -------
    result : int
        文字列中の数字の桁数
    """

    result = 0
    results = []
    # 正規パターンをセット
    regex = re.compile('\d+')

    # 文字列中の数字を抽出し配列として定義
    for line in text.splitlines():
        results = regex.findall(line)

    if results == []:
        # 文字列に数字が存在しなかった場合
        result = 0
    else:
        # 文字列に数字した場合、総計をカウント
        for digits_num in results:
           result = result + len(digits_num)

    return result


"""
ex:

# 文字列を1文字ずつ配列として考え、チェックし数字だった場合カウントアップする。
def count_digits(text: str) -> int:
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count

---

def count_digits(text: str) -> int:
    return(sum(i.isdigit()for i in text))


"""

