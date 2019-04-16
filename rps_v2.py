from random import randint

# # Asking for Player 1's Choice
p_choice = input("Player 1, make your move: ").lower()

#randomizer for computer behavior
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"The computer plays {computer}")


# Refined Game Logic
if p_choice == "rock" or p_choice == "paper" or p_choice == "scissors":
    if p_choice == computer:
        print("It's a tie!")
    elif p_choice == "rock":
        if computer == "scissors":
            print("Player is the winner!")
        else:
            print("The computer is the winner!")
    elif p_choice == "paper":
        if computer == "rock":
            print("Player is the winner!")
        else:
            print("The computer is the winner!")
    elif p_choice == "scissors":
        if computer == "paper":
            print("Player is the winner!")
        else:
            print("The computer is the winner!")
else:
    print("Please Enter 'Rock', 'Paper', or 'Scissors'")