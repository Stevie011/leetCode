class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            #row check
        for i in range(len(board)):
            currentRowNums = []
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    #skips it if the current entry is "."
                    continue
                else:
                    #else add it to current temp list
                    currentRowNums.append(int(board[i][j]))
            #convert to list to check for duplicates
            if len(currentRowNums) != len(set(currentRowNums)):
                #list removes dups, so len() will be different
                return False
        #column check
        for i in range(9):
            currentColNums = []
            for j in range(9):
                if board[j][i] == ".":
                    continue
                else:
                    currentColNums.append(int(board[j][i]))
            if len(currentColNums) != len(set(currentColNums)):
                return False
        #you could also do this by adding every value to a list and then splicing the lists
        #square by square check
        #top left
        #this topLeftSquare should be called currentSquare
        topLeftSquare = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ".":
                    continue
                else:
                    topLeftSquare.append(int(board[i][j]))
            if len(topLeftSquare) != len(set(topLeftSquare)):
                return False

        #top middle
        topLeftSquare = []
        for i in range(3):  
            for j in range(3,6):
                if board[i][j] == ".":
                    continue
                else:
                    topLeftSquare.append(int(board[i][j]))
            if len(topLeftSquare) != len(set(topLeftSquare)):
                return False

        topLeftSquare = []

        #top right
        for i in range(3):  
            for j in range(6,9):
                if board[i][j] == ".":
                    continue
                else:
                    topLeftSquare.append(int(board[i][j]))
            if len(topLeftSquare) != len(set(topLeftSquare)):
                return False

        topLeftSquare = []
        
        #left mid
        for i in range(3,6):  
            for j in range(3):
                if board[i][j] == ".":
                    continue
                else:
                    topLeftSquare.append(int(board[i][j]))
            if len(topLeftSquare) != len(set(topLeftSquare)):
                return False

        topLeftSquare = []

        #mid mid
        for i in range(3,6):  
            for j in range(3,6):
                if board[i][j] == ".":
                    continue
                else:
                    topLeftSquare.append(int(board[i][j]))
            if len(topLeftSquare) != len(set(topLeftSquare)):
                return False

        topLeftSquare = []

        #mid mid
        for i in range(3,6):  
            for j in range(6,9):
                if board[i][j] == ".":
                    continue
                else:
                    topLeftSquare.append(int(board[i][j]))
            if len(topLeftSquare) != len(set(topLeftSquare)):
                return False

        topLeftSquare = []

        #bottom left 
        for i in range(6,9):  
            for j in range(3):
                if board[i][j] == ".":
                    continue
                else:
                    topLeftSquare.append(int(board[i][j]))
            if len(topLeftSquare) != len(set(topLeftSquare)):
                return False

        topLeftSquare = []

        #bottom mid
        for i in range(6,9):  
            for j in range(3,6):
                if board[i][j] == ".":
                    continue
                else:
                    topLeftSquare.append(int(board[i][j]))
            if len(topLeftSquare) != len(set(topLeftSquare)):
                return False

        topLeftSquare = []

        #bottom right
        for i in range(6,9):  
            for j in range(6,9):
                if board[i][j] == ".":
                    continue
                else:
                    topLeftSquare.append(int(board[i][j]))
            if len(topLeftSquare) != len(set(topLeftSquare)):
                return False

        topLeftSquare = []

        #if it passes all the rest, it must be valid
        return True
