"""
Challenge 3: Guessing Game

Generate a random number from 1–20.

Keep asking until the user guesses correctly.

Afterward print:

Correct!

It took you 6 guesses.

Practice:

loops
break
random module

"""

import random

randint = random.randint(1, 20)
guess = -1
attempts = 0
while randint != guess:
    guess = int(input("Enter a random number between 1-20: "))
    while guess < 1 or guess > 20:
        guess = int(input("Invalid input. Enter a random number between 1-20: "))
    attempts += 1

print(f"Congrats! The correct answer was {randint}. \nIt took you {attempts} attempts to guess it correctly!")