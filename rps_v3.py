from random import randint
player_wins = 0
computer_wins = 0
winning_score = input("Enter the winning score for the game: ")
winning_score = int(winning_score)

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player's Score: {player_wins}  Computer's Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    p_choice = input("Player 1, make your move: ").lower()
    if p_choice == "quit" or p_choice == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"The computer plays: {computer}")

    # Refined Game Logic
    if p_choice == "rock" or p_choice == "paper" or p_choice == "scissors":
        if p_choice == computer:
            print("It's a tie!")
        elif p_choice == "rock":
            if computer == "scissors":
                print("Player is the winner!")
                player_wins += 1
            else:
                print("Computer is the winner!")
                computer_wins += 1
        elif p_choice == "paper":
            if computer == "rock":
                print("Player is the winner!")
                player_wins += 1
            else:
                print("Computer is the winner!")
                computer_wins += 1
        elif p_choice == "scissors":
            if computer == "paper":
                print("Player is the winner!")
                player_wins += 1
            else:
                print("Computer is the winner!")
                computer_wins += 1
    else:
        print("Please Enter 'Rock', 'Paper', or 'Scissors'")

if player_wins > computer_wins:
    print("Congrats, you've defeated the Computer!")
elif player_wins == computer_wins:
    print("It's a Tie!")
else:
    print("Oh No! The Computer is victorious!")


