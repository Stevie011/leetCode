class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #std format for checking rows and columsn of grid
        r,c = len(mat), len(mat[0])
        #use set to make sure we don't visit same one twice
        visited = set()
        #study deque
        q = deque()

        #nested loops to go thru every cell
        for i in range(r):
            for j in range(c):
                #if it's a zero cell
                if mat[i][j] == 0:
                    #add the co-ords to visited
                    visited.add((i,j))
                    #also add the to the q
                    q.append((i,j))

        #while there are vals in the q
        while q:
            r2,c2 = q.popleft()
            #this checks all 4 directions
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                row,col = r2+dr, c2+dc
                #check if its within bounds and not yet been visited
                if r>row>=0 and c>col>=0 and (row,col) not in visited:
                    mat[row][col] =mat[r2][c2]+1
                    visited.add((row,col))
                    q.append((row,col))
        return mat
