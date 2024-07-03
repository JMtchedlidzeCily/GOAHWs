import random

correct_answer = random.randint(1, 10)
guess = 0

while guess != correct_answer:
    guess = int(input("Guess the dice roll (1-10): "))
    if guess == correct_answer:
        print("It's correct!")
    else:
        print("It's incorrect.")

