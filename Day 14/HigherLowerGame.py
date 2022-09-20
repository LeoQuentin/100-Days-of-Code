from game_data import data
from art import logo, vs
import random


gameStillRuns = True
global currentCeleb; global opposingCeleb
celebName = ""; celebFollowerCount = ""; celebDescription = ""; celebCountry = ""
currentCeleb = random.randint(0,len(data)-1)
opposingCeleb = random.randint(0,len(data)-1)

global score; score = 0



def chooseNewCeleb():
    global opposingCeleb
    while opposingCeleb == currentCeleb:
        opposingCeleb = random.randint(0,len(data))


chooseNewCeleb()

def formatToVariables(profile):
    celebData = data[profile]
    celebName = celebData["name"]
    celebFollowerCount = celebData["follower_count"]
    celebDescription = celebData["description"]
    celebCountry = celebData["country"]
    return(f"{celebName}, a {celebDescription.lower()} from {celebCountry}")

while gameStillRuns == True:
    print(logo)
    print("Compare A: " + formatToVariables(currentCeleb))
    print(vs)
    print("Against B: " + formatToVariables(opposingCeleb))
    AorB = input("Who has more followers? Type \'A\' or \'B\': ")
    if AorB.upper() == "A":
        if data[currentCeleb]['follower_count'] > data[opposingCeleb]['follower_count']:
            print(logo)
            score += 1
            print(f"You're right! Current score: {score}")
            currentCeleb = opposingCeleb
            chooseNewCeleb()
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    elif AorB.upper() == "B":
        if data[currentCeleb]['follower_count'] < data[opposingCeleb]['follower_count']:
            print(logo)
            score += 1
            print(f"You're right! Current score: {score}")
            currentCeleb = opposingCeleb
            chooseNewCeleb()
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    

