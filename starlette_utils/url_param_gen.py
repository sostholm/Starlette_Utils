# A simple generator function
def url_param_gen(url_params: dict):
    """Orders url param dict

    Parameters
    ----------
    url_params : dict
        contains the url parameters

    Yields
    -------
    dictionary pair {key: param}
    """

    next_param = ''
    num = 1
    while next_param is not 'end':
        key = f"param{num}"
        next_param = url_params.get(key, "end")
        if next_param is not 'end':
            yield {key: next_param}
            num += 1


if __name__ == '__main__':
    test = {"param1": 'p1', "param2": 'p2', "param3": 'p3'}
    for param in url_param_gen(test):
        print(param)