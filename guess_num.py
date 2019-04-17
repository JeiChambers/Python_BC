from random import randint

r_num = randint(1, 10) #randint is inclusive
# Handles User Guesses

while True:
    guess = input("Please guess a number between 1 and 10: ")
    guess = int(guess)

    if guess < r_num:
        print("Oops your guess is too low! Try again!")
    elif guess > r_num:
        print("Oops, your guess is too high! Try again!")
    else:
        print("Congratulations! You've guessed correctly!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == 'y':
            r_num = randint(1, 10)
            guess = None
        else:
            print("Thanks for playing!")
            break

