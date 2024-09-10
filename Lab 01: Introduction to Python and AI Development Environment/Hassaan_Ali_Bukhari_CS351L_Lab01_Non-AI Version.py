import random

def number_guessing_game():
    # The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Player has 10 attempts to guess the number
    
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100. You have 10 attempts.")

    # Loop for the player to make guesses
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return

    print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

# Run the game
number_guessing_game()