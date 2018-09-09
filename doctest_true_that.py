def true_that():
    """
    >>> true_that()
    True
    """
    return True


# Should work but doctest actually orders the dict which isn't necessary
def make_dict(keys):
    """
    >>> make_dict(['a', 'b'])
    {'b': True, 'a': True}
    """
    return {key: True for key in keys}
