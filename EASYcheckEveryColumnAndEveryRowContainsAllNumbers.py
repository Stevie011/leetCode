class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        for row in matrix:
            #this removes duplicates
            if len(set(row)) != n:
                return False
                
        #new matrix for columns. gotta learn this better
        #https://www.youtube.com/watch?v=6l0_5Weq-3k
        #dictionary comprehension!!!
        #flipped the columns into rows for newMatrix
        newMatrix = [[None]* n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                newMatrix[x][y] = matrix[y][x]
        
        #do the same thing we did for the rows on top       
        for row in  newMatrix:
            if len(set(row)) != n:
                return False
        
        return True
        