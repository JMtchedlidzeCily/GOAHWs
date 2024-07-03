import random

# Randomly choose a correct answer between 1 and 6
correct_answer = random.randint(1, 6)

# Get the user's guess
guess = int(input("Guess the dice roll (1-6): "))

# Check if the guess is correct
if guess == correct_answer:
    print("It's correct!")
else:
    print("It's incorrect. The correct answer was", correct_answer)
