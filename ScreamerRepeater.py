how_many_times = int(input("How many times do I have to tell you? "))

# for i in range(1, how_many_times):
#     print('CLEAN UP YOUR ROOM!')
#     if i == 5:
#         break


for i in range(1, how_many_times):
    print('CLEAN UP YOUR ROOM!')
    if i >= 4:
        print('Do you even listen anymore?')
        break
