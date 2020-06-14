def bigger_price(limit: int, data_list: list) -> list:
    """
    商品の中で高額の商品を降順に抽出する。

    Parameters
    ----------
    limit : int
        抽出する商品の個数
    data_list : list
    高額商品のリスト
        - key(商品名) : value(値段) : dict

    Returns
    -------
    result : list
    高額商品のリスト(降順)
        - key(商品名) : value(値段) : dict
    """

    return sorted(data_list, reverse=True, key=lambda x: x['price'])[0:limit]

"""
ex:
return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]

"""

