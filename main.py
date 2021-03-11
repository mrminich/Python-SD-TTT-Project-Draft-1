# YOUR NAME HERE
# Works Cited
# None

##### imports

import gameFunctions
import ioFunctions
import consoleDisplay

gameStateTest = [
  0, 0, -1, 
  0, 1, 0,
  1, 0, -1
]
consoleDisplay.display2DBoard(gameStateTest)
quit()

##### constants

# indicates that the user wants to quit the game
SENTINEL = -1

##### variables

# debugging mode for developer
debug = False

# game variables

# game is currently in play or not
gameInPlay = True

# user prompt to input their next move
prompt = "Enter a value between 1 and 9 (" + str(SENTINEL) + " to quit): "

# the tic tac board with player entries
gameState = [
  0, 0, 0, 
  0, 0, 0,
  0, 0, 0
]

# total number of turns taken between both players
numTurns = 0

##### functions

def main():
  global numTurns

  # main game logic

  print("hello, game is started...")

  while gameInPlay:
    print("in play")

    # next player's turn
    numTurns += 1 

    if debug:
      print("debugging....")
      print(gameState)
      print("turn # " + str(numTurns))

    print(ioFunctions.getBasicBoard(gameState))
    userInput = ioFunctions.getIntegerInput(prompt)


    # user wants to exit     
    if userInput == SENTINEL:
      break
    elif not (userInput > 0 and userInput < 10):
      print("invalid input " + str(userInput))
    else:
      print("processing move")

      if numTurns % 2 == 1: 
        # X's turn
        gameState[userInput - 1] = 1
      else: # elif numTurns % 2 == 0:
        # O's turn
        gameState[userInput - 1] = -1

      if gameFunctions.isThereAWin(gameState):
        print("there is a winner")
        break
      else:
        print("there is not a winner")


  print("goodbye, game is over")
  print(ioFunctions.getBasicBoard(gameState))

##### main

if __name__ == "__main__":
  main()