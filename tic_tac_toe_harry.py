def sum(a, b, c):
  return a + b + c

def printboard(xState, zState):
  # print(f"0 | 1 | 2 ")
  # print(f"--|---|---")
  # print(f"3 | 4 | 5 ")
  # print(f"--|---|---")
  # print(f"6 | 7 | 8 ")

  zero = 'X' if xState[0] else 'O' if zState[0] else 0
  one = 'X' if xState[1] else 'O' if zState[1] else 1
  two = 'X' if xState[2] else 'O' if zState[2] else 2
  three = 'X' if xState[3] else 'O' if zState[3] else 3
  four = 'X' if xState[4] else 'O' if zState[4] else 4
  five = 'X' if xState[5] else 'O' if zState[5] else 5
  six = 'X' if xState[6] else 'O' if zState[6] else 6
  seven = 'X' if xState[7] else 'O' if zState[7] else 7
  eight = 'X' if xState[8] else 'O' if zState[8] else 8
  print(f"{zero} | {one} | {two} ")
  print(f"--|---|---")
  print(f"{three} | {four} | {five} ")
  print(f"--|---|---")
  print(f"{six} | {seven} | {eight} ")

def checkForWin(xState, zState):
  #print(f"checkForWin invoked")
  wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
  for win in wins:
    if(sum(xState[win[0]], xState[win[1]], xState[win[2]])) == 3:
      print(f"X won the game")
      return 1
    if(sum(zState[win[0]], zState[win[1]], zState[win[2]])) == 3:
      print(f"O won the game")
      return 0
  if(sum(xState.count(1), zState.count(1), 0) == 9):
    print("Game ended in a tie")
    return -2
  return -1

def isSpotFree(play_spot, xState, zState):
  """
  Given a spot where the user wants to play (place X or O), it checks if this spot is already occupied by previous move played during the game
  Returns True if the spot is free else False
  """
  if xState[play_spot] == 1 or zState[play_spot] == 1:
    return False
  return True

def isSpotInRange(spotInt):
  """
  Player needs to enter a spot in the range 0 till 8
  """
  return 0 <= spotInt <= 8

if __name__ == '__main__':
  xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  print(f"\nWelcome to Tic Tac Toe game:")
  playerOneName = input("Enter 1st player name: ")
  playerTwoName = input("Enter 2nd player name: ")
  player_dict = {"0": playerOneName, "1": playerTwoName}
  #print(player_dict)
  turn = 1 # 1 for X and 0 for O
  printboard(xState, zState)
  while True:
    #print(f"Entered in the while loop")
    hasPlayedMadeMove = False
    if turn == 1 and hasPlayedMadeMove == False:
      print("X's turn:")
      print("{}'s turn".format(player_dict["0"]))
      try:
        play_spot = int(input("Enter a number from 0 to 8: "))
      except ValueError:
        print(f"Enter a valid value (0-8)")
        continue
      if not isSpotInRange(play_spot):
        print(f"Enter valid number (0 - 8). Try again")
        continue
      if isSpotFree(play_spot, xState, zState):
        xState[play_spot] = 1
        hasPlayedMadeMove = True
      else:
        print(f"The spot is already occupied. Try again")
        turn = 0
        hasPlayedMadeMove = False
    else:
      print("O's turn:")
      print("{}'s turn".format(player_dict["1"]))
      play_spot = int(input("Enter a number from 0 to 8: "))
      try:
        play_spot = int(input("Enter a number from 0 to 8: "))
      except ValueError:
        print(f"Enter a valid value (0-8)")
        continue
      if not isSpotInRange(play_spot):
        print(f"Enter valid number (0 - 8). Try again")
        continue
      if isSpotFree(play_spot, xState, zState):
        zState[play_spot] = 1
        hasPlayedMadeMove = True
      else:
        print(f"The spot is already occupied. Try again")
        turn = 1
        hasPlayedMadeMove = False
    printboard(xState, zState)
    if hasPlayedMadeMove:
      checkWin = checkForWin(xState, zState)
      #print(f"checkwin: {checkWin}")
      # if(checkWin != -1):
      #   #printboard(xState, zState)
      #   break
      if checkWin in range(2):
        print("{} won the game".format(player_dict[str(1 - checkWin)]))
        break
      elif checkWin == -2:
        break
    turn = 1 - turn

