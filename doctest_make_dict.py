# Should work but get this:  Got: {'a': True, 'b': True}
# Needed to change test from 'b', 'a' to 'a' 'b'
def make_dict(keys):
    """
    >>> make_dict(['a', 'b'])
    {'a': True, 'b': True}
    """
    return {key: True for key in keys}


