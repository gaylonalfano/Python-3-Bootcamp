def multiple_letter_count(word):
    """
    >>> multiple_letter_count("  ")
    {' ': 2}
    """
    return {letter: word.count(letter) for letter in set(word)}

print(multiple_letter_count("  "))