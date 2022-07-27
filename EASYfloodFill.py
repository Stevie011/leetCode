
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #set row and column sizes
        r,c = len(image), len(image[0])
        #put start color in another variable (coz we gonna change it)
        startCol = image[sr][sc]
        
        #bring in the recursive dfs
        def dfs(i,j):
            #check if it's within the borders, and if the color matches
            if r > i >= 0 and c > j >= 0 and image[i][j] == startCol:
                #change the color
                image[i][j] = color
                #go all four directions
                return dfs(i+1, j) and dfs(i-1, j) and dfs(i, j+1) and dfs(i,j-1)
            #if earlier conds not met, we can return img unaltered
            return image
        
        #nb-could be  case where both colors are the same: infinite loop
        if startCol != color:
            #start the dfs recursion here then
            image = dfs(sr,sc)
        #once all changes are done, put image back out    
        return image