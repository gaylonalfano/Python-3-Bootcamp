'''
zip - It exhausts after one use. Make an iterator that aggregates elements from each of the iterables. Returns an interator of tuples (list),
where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
The iterator stops when the shortest input iterable is exhausted, meaning that the lengths don't truly have
to be the same. However, it will zip the two lists until the shortest list is exhausted/used up.

Imagine we have two list of numbers of the exact same length. Zip will make a new list where it pairs up
the first number from the first list to the first number in the second list, etc. Just like a zipper!

It's not limited to just two iterables! You can have multiple iterables you pass to zip and it will
zip the pairings until the shortest list has been exhausted.

'''

first_zip = zip([1, 2, 3], [4, 5, 6])  # Returns a zip object
# print(list(first_zip))  # [(1, 4), (2, 5), (3, 6)]
# print(dict(first_zip))  # {1: 4, 2: 5, 3: 6}


nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
nums3 = [11, 12, 13, 14, 15]
words = ['hi', 'hola', 'lol', ':)']

z = zip(nums1, nums2)
y = zip(nums1, nums3)
w = zip(words, nums3, nums2)

print(list(z))  # [(1, 6), (2, 7), etc.]
print(dict(y))  # {1: 11, 2: 12, 3: 13, ...}
print(list(w))  # [('hi', 11, 6), ('hola', 12, 7), ('lol', 13, 8), ...]

'''
You can also use the * operator to unpack a list of tuples. Pass them individually. 
Pretty common when we work with more complex data structures. Remember to do that for a list/tuple, 
just add * in front of the list/tuple. For dict, add ** to unpack.
'''

five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
list(zip(*five_by_two))  # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]


# How to create a dict that matches the student with their highest test score?
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# My attempt before tutorial:
def top_score(nums1, nums2, students):
    high_score = []
    for i in zip(nums1, nums2):
        high_score.append(max(i))
#print(high_score)
    return dict(zip(students, high_score))


print(top_score(midterms, finals, students))
print(top_score((85, 98, 77), (90, 88, 83), ('Archie', 'Aaron', 'Adrian')))


# Instructor's LIST/DICT COMPREHENSION: We want a dict like this: {"dan": 98, 'ang': 91, etc.}
# final_grades = [max(pair) for pair in zip(midterms, finals)]  # just add max(pair) in front
# final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}


# Instructor's ZIP/MAP/LAMBDA: Map - tell it the collection to map and how we want it to be mapped (based on max)
# scores = map(lambda pair: max(pair), zip(midterms, finals))
# print(list(scores))  # [98, 91, 78]. Now take this and zip it again but with students
# final_grades = dict(
#     zip(
#         students,
#         map(
#             lambda pair: max(pair),
#             zip(midterms, finals)
#         )
#     )
# )

# Above can be rewritten as:
final_grades = dict(zip(students, map(lambda x: max(x), zip(midterms, finals))))
# print(final_grades)

# What if we wanted to return the AVERAGE instead?
avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0] + pair[1])/2),
            zip(midterms, finals)
        )
    )
)

# Student sample from forums:
print({k:v for k,v in zip(students,[max(arr) for arr in zip(midterms,finals)])})

print(avg_grades)


'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']

Could try to iterate over the list and .get('first') and .get('last')??
'''

def extract_full_name(list_of_dicts):
    return [' '.join(i.values()) for i in list_of_dicts]


# Instructor's solution:
def extract_full_name2(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]))

