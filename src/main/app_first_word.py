def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    # 前後に余計なピリオドがあった場合除去
    result = text.strip('.')
    # 前後の空白を除去
    result = result.split()[0]
    # 文中にカンマがあった場合除去し最初の文字を取得
    if ',' in result:
        result = result.split(',')[0]
    # 文中にピリオドがあった場合は除去し最初の文字を取得
    if '.' in result:
        result = result.split('.')[0]

    return result


# best practice
'''
def first_word(text: str) -> str:
    return text.replace(',',' ').replace('.',' ').split()[0]

def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ').strip()
    return text.split()[0]

import re
def first_word(input_string: str) -> str:
    return re.sub(r"[.,]", " ", input_string).split()[0]


'''