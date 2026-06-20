#NUMBER GUESSING GAME

import random
secret_number = random.randint(1, 100)

# Maximum number of attempts
max_attempts = 7


print("NUMBER GUESSING GAME")

print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")
print("_" * 45)


for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input(f"\nAttempt {attempt}/{max_attempts} - Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try entering a higher number.")

        elif guess > secret_number:
            print("Too high! Try entering a lower number.")

        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} correctly.")
            print(f"You took {attempt} attempt(s).")
            break

    except ValueError:
        print("Invalid input! Please enter a valid number.")

else:
    print("Game Over!")
    print(f"The correct number was: {secret_number}")