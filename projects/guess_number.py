# Guess the Number Game
# The computer picks a random number and the player tries to guess it

import random

# Pick a random number between 1 and 100 (inclusive)
secret_number = random.randint(1, 100)

# Track how many guesses the player has made
attempts = 0

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")
print()

# Keep looping until the player guesses correctly
while True:
    # Ask the player for their guess
    user_input = input("Your guess: ")

    # Convert the input string to an integer
    # (input() always returns a string, so we need int())
    guess = int(user_input)

    # Count this as one attempt
    attempts += 1

    # Compare the guess to the secret number and give a hint
    if guess < secret_number:
        print("Too low! Try higher.")
    elif guess > secret_number:
        print("Too high! Try lower.")
    else:
        # Exact match — the player wins
        print(f"Correct! You guessed it in {attempts} attempt(s).")
        break  # Exit the loop since the game is over
