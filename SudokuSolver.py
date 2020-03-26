import solver

puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8] 
    
#open puzzle.txt
f = open("puzzleZero.txt", "r")

#read in 9 lines of the text file
i = 0
while i != 9:
    puzzle[i] = f.readline()
    i += 1
    
#close puzzle.txt
f.close()



#init solver class
s = solver.solver(puzzle) 
#s.printPuzzle()
s.printPuzzleRec(0, 0)

print("does exist: " , s.checkRow(1, 8))




