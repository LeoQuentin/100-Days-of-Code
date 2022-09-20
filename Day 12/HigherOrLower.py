import random
correctNumber = random.randint(0,101)
global hasLost
hasNotWon = True

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {correctNumber}")
difficultyString = input("Choose a difficulty. Type 'easy' or 'hard': ")


global triesLeft
if difficultyString.lower() == "easy":
    triesLeft = 10
else:
    triesLeft = 5

while triesLeft > 0:
    print(f"You have {triesLeft} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == correctNumber:
        print(f"You got it! The answer was {correctNumber}.")
        hasNotWon = False
        break
    elif guess > correctNumber:
        print("Too high.")
        triesLeft -= 1
        if triesLeft > 0:
            print("Guess again")
    elif guess < correctNumber:
        print("Too high.")
        triesLeft -= 1
        if triesLeft > 0:
            print("Guess again")
if hasNotWon == True:
    print("You suck at this")