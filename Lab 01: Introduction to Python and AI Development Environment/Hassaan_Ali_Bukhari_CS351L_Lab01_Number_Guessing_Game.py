"""For a basic implementation of the Number Guessing Game using a search strategy, we can use a simple algorithm like Binary Search. Binary Search is efficient and easy to understand, making it a great choice for beginners."""

import random

def number_guessing_game():
    # Define the range for the guessing game
    lower_bound = 1
    upper_bound = 100
    attempts = 0
    
    # Generate a random number between the defined range
    target_number = random.randint(lower_bound, upper_bound)
    
    print("Welcome to the Number Guessing Game!")
    print(f"Guess the number between {lower_bound} and {upper_bound}.")

    # Binary Search Algorithm
    while True:
        # Prompt the user for their guess
        guess = int(input(f"Enter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess == target_number:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Run the game
number_guessing_game()
