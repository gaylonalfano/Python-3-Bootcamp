# def make_song(num_of_beverage=3, beverage='soda'):
#     count = num_of_beverage
#     while True:
#         if count > 1:
#             yield f"{count} bottles of {beverage} on the wall."
#             count -= 1
#         elif count == 1:
#             yield f"Only {count} bottle of {beverage} left!"
#             count -= 1
#         else:
#             yield f"No more {beverage}!"
#             raise StopIteration



# This works AND it was EXACTLY like Colt's:
def make_song2(number=99, beverage='soda'):
    for n in range(number, -1, -1):  # range(start, stop (exclusive), step)
        if n > 1:
            yield "{} bottles of {} on the wall.".format(n, beverage)  # "{n} bottles of {beverage} on the wall."
        elif n == 1:
            yield "Only {} bottle of {} left!".format(n, beverage)  # "Only {n} bottle of {beverage} left!"
        else:
            yield "No more {}!".format(beverage)  # "(f"No more {beverage}!")


# Another solution:
# def make_song(count=99, beverage='soda'):
#     for f in range(count - 1):
#         yield f'{count - f} bottles of {beverage} on the wall.'
#     yield f'Only 1 bottle of {beverage} left!'
#     yield f'No more {beverage}'




#
# song1 = make_song2()
#
# print(next(song1))
# print(next(song1))
# print(next(song1))
# print(next(song1))
# print(next(song1))

# kombucha_song = make_song2(5, 'kombucha')
#
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))
# print(next(kombucha_song))




default_song = make_song()

print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))


