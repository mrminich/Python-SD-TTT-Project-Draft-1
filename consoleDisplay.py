def display2DBoard(gameState):
  counter = 0

  for row in range(len(gameState)):
    
    if counter == 3 or counter == 6:
      print()
      print("----------")

    if counter != 3 and counter != 6: 
      print(str(gameState[counter]) + " | ", end="")

    counter += 1