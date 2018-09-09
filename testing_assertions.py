# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y
#
#
# print(add_positive_numbers(1, 1)) # 2
# add_positive_numbers(1, -1)  # AssertionError: Both numbers must be positive!


def eat_junk(food):
    assert food in ['pizza',
                    'ice cream',
                    'candy',
                    'fried butter'
                    ], "Food must be a junk food!"
    return f"NOM NOM NOM I am eating {food}"

food = input("Enter a food please: ")
print(eat_junk(food))


# ASSERTIONS WARNING - Optimized Mode -O example: Check if a user is an admin
# If you ran the below with -O then any user could destroy stuff.
def do_something_bad(user):
    assert user.is_admin, "Only admins can do bad things!"
    destroy_a_bunch_of_stuff()
    return "Mua ha ha ha!"