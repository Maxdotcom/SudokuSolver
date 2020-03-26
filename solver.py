class solver:
  def __init__(self, puzzle):
    self.puzzle = puzzle

  def printPuzzle(self):
    for i in range(9):
      print("")
      for j in range(9): 
        print(self.puzzle[i][j], end=" ")
    print("")

  def printPuzzleRec(self, i, j):
    if  i >= 8 and j >= 8:
      print(self.puzzle[i][j])
      print("DONE")
      return 1  
    elif i < 9 and j < 9:
      print(self.puzzle[i][j], end=" ")
      self.printPuzzleRec(i, j+1)
    elif i < 9 and j >= 8:
      print(" ")
      self.printPuzzleRec(i+1, 0)
    elif i >= 8 and J < 9:
      print(self.puzzle[i][j], end=" ")
      self.printPuzzleRec(i, j+1)
    else:
      print(self.puzzle[i][j], end=" ")

      


  def checkRow(self, n, i):
    if i < 9:
      for j in self.puzzle[i]:
        print("j: " , j , "n: " , n)
        #if j == n and type(j) != str:
        if int(j) == n:
          print("TRUE")
          return 1
        else:
          print("FALSE")
    else:
      print("number greater than 9")
      return 0
    
 