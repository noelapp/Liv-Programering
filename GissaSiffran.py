# Välja ett tal

correctNumber = 6
numOfGuesses = 3

# Be om en siffra

while (numOfGuesses > 0):
    print("guess a number")
    guess = int(input())
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