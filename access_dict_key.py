import random

# playerOneName = input("Enter 1st player name: ")
# playerTwoName = input("Enter 2nd player name: ")
playerOneName = "Abhikriti"
playerTwoName = "Abhishek"
player_dict = {"0": playerOneName, "1": playerTwoName}
print(player_dict)

def checkForWin():
  return random.randint(0,1)

checkWin = checkForWin()
print(checkWin)
print(f"{player_dict[str(checkWin)]} won")
print("{}'s turn. Your name is {}".format(player_dict["0"], player_dict[str(checkWin)]))