'''
Write a function interleave() that accepts two strings. It should return a new string containing
the two strings interwoven or zipped together. For example:

interleave('hi', 'ha')  # 'hhia'
interleave('aaa', 'zzz')  # 'azazaz'
interleave('lzr', 'iad')  # 'lizard'

'''


def interleave(str1, str2):
    return ''.join(
        map(
            lambda i: i[0] + i[1],
            zip(str1, str2)
        )
    )


def interleave(str1, str2):
    return ''.join(map(lambda i: i[0]+i[1], zip(str1, str2)))


# Instructor's code:
def interleave2(str1, str2):
    return ''.join(''.join(x) for x in (zip(str1, str2)))

print(interleave('aaa', 'zzz'))

print(interleave('lzr', 'iad'))


