# Frågesport

import random


correctNumber = random.randint(1, 10)
numOfGuesses = 10

print("Welcome to my guessing game!")
print("guess the right number and you win!!")

# Be om en siffra

while (numOfGuesses > 0):
    
    print("Guess a number below :)")
    guess = input()
    print("you guessed")
    print(guess)

    numOfGuesses -= 1
    # Kolla om siffran är större, eller mindre, lika

    if (guess > correctNumber):
        print("You guessed to high, try again.")
    elif (guess < correctNumber):
        print("You guessed to low, try again.")
    else:
        print("You guessed right! Good job")
        numOfGuesses = 0 


# göra tre gånger