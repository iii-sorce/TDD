def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    result = text.split()[0]
    if ',' in result:
        result = result.split(',')[0]
    return result