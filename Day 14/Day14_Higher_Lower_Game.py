from game_data import data
import random
print("hello")

game_still_runs = True

global current_B
print (data[1]["name"])

def selectRandomDictionary():
    chosenDictionary = data[random.randint(0, len(data)-1)]
    if chosenDictionary == current_A:
        selectRandomDictionary()
    return chosenDictionary

global current_A
current_A = selectRandomDictionary

while game_still_runs:



# print(f"You're right! Current score {current_score})
