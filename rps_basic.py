# # Asking for Player 1's Choice
# p1_choice = input("Player 1, please enter your choice: ")

# # Taking up space on the screen so Player 2 can't see Player 1's choice.
# i = 0
# while i < 10:
#     print("******* NO CHEATING, PLAYER 2 *******")
#     i += 1
# # Asking for Player 2's Choice
# p2_choice = input("Player 2, please enter your choice: ")

# #Game Logic
# if p1_choice and p2_choice:
#     if p1_choice == "rock" and p2_choice == "scissors":
#         print("Player 1 is the winner!")
#     elif p1_choice == "scissors" and p2_choice == "paper":
#         print("Player 1 is the winner!")
#     elif p1_choice == "paper" and p2_choice == "rock":
#         print("Player 1 is the winner!")
#     elif p1_choice == "scissors" and p2_choice == "rock": 
#         print("Player 2 is the winner!")
#     elif p1_choice == "paper" and p2_choice == "scissors":
#         print("Player 2 is the winner!")
#     elif p1_choice == "rock" and p2_choice == "paper":
#         print("Player 2 is the winner!")
#     elif p1_choice == p2_choice:
#         print("It's a draw! O.O")
#     else:
#         print("Please use Lower Case words")
# else:
#     print("Please Enter a Choice: ")

##################################################################

#Code Refactored

# Asking for Player 1's Choice
p1_choice = input("Player 1, please enter your choice: ")

# Taking up space on the screen so Player 2 can't see Player 1's choice.
i = 0
while i < 20:
    print("******* NO CHEATING, PLAYER 2 *******\n")
    i += 1
# Asking for Player 2's Choice
p2_choice = input("Player 2, please enter your choice: ")

#Game Logic (Imperfect as bogus entry for Player 2 will break code.)
if p1_choice and p2_choice:
    if p1_choice == p2_choice:
        print("It's a tie!")
    elif p1_choice == "rock":
        if p2_choice == "scissors":
            print("Player 1 is the winner!")
        elif p2_choice == "paper":
            print("Player 2 is the winner!")
    elif p1_choice == "paper":
        if p2_choice == "rock":
            print("Player 1 is the winner!")
        elif p2_choice == "scissors":
            print("Player 2 is the winner!")
    elif p1_choice == "scissors":
        if p2_choice == "paper":
            print("Player 1 is the winner!")
        elif p2_choice == "rock":
            print("Player 2 is the winner!")
else:
    print("Please Enter a Choice: ")

