def backward_string_by_word(text: str) -> str:
    """
    与えられた文字列を反転する　ただし単語の位置は変更しない

    Parameters
    ----------
    text : str
        ランダムな文字列

    Returns
    -------
    result : int
        ランダムな文字列を反転したもの
    """
    #
    # # TODO　スペースで区切られた場合 分割　list
    # results = text.split()
    #
    # reversal_list = []
    # # TODO 分割した単語を先頭から
    # for l in results:
    #     reversal_list.append(l[::-1])
    #
    # result = ' '.join(reversal_list)
    #
    # return result

    for i in text.split():
        text = text.replace(i, i[::-1])
    return text

"""
ex:
def backward_string_by_word(text: str) -> str:
    for i in text.split():
        text = text.replace(i,i[::-1])    
    return text

def backward_string_by_word(text: str) -> str:
    return " ".join([i[::-1] for i in text.split(" ")])

"""

