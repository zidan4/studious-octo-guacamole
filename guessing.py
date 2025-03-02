
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Try to guess it!")

while True:
    # Get user guess
    guess = int(input("Enter your guess: "))

    # Check the guess
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed the number {secret_number} correctly!")
        break  # Exit the loop when guessed correctly
