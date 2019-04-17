# for smile in range(1, 11):
#     print("\U0001f600" * smile)


# # Nested For Loop
# for x in range(3):
#     for num in range(1,11):
#         print("\U0001f600" * num)

# # Emoji Art using While Loop
# # smirk = 1
# # while smirk < 11:
# #     print("\U0001f600" * smirk)
# #     smirk += 1

# Making an Emoji Pyramid
for smile in range(1, 22, 2):
    if smile == 1:
        print(" " * 10  + "\U0001f600" * smile)
    elif smile == 3:
        print(" " * 9  + "\U0001f600" * smile)
    elif smile == 5:
        print(" " * 8 + "\U0001f600" * smile)
    elif smile == 7:
        print(" " * 7  + "\U0001f600" * smile)
    elif smile == 9:
        print(" " * 6 + "\U0001f600" * smile)
    elif smile == 11:
        print(" " * 5  + "\U0001f600" * smile)
    elif smile == 13:
        print(" " * 4 + "\U0001f600" * smile)
    elif smile == 15:
        print(" " * 3  + "\U0001f600" * smile)
    elif smile == 17:
        print(" " * 2 + "\U0001f600" * smile)
    elif smile == 19:
        print(" " * 1  + "\U0001f600" * smile)
    else:
        print("\U0001f600" * smile)
