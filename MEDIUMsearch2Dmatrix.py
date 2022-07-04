class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #get number of rows and columns
        rows, cols = len(matrix), len(matrix[0])

        #then get left and right pointers
        left, right = 0, rows-1
        #if left > right, the search would overlap
        while left <= right:
            #binary time
            currentRow = (left + right) //2
            #check if target is greater than right most value of current row
            #if it is, we know it's not in that row, coz the matrix is sorted
            # we use [-1] index to ref last value
            if target > matrix[currentRow][-1]:
                #if it is greater, move right/down the list
                left = currentRow + 1
            #other way around
            elif target < matrix[currentRow][0]:
                right = currentRow - 1
            #if it's not either, it must fall in the current row
            else:
                break
        #if the value isn't incld in any rows, we can return false
        if not (left <= right):
            return False
        #second binary search on row
        currentRow = (left + right) //2
        l,r = 0, cols-1
        while l<=r:
            m = (l+r)
            if target > matrix[currentRow][m]:
                l = m+1
            elif target < matrix[currentRow][m]:
                r = m-1
            else:
                return True
        return False
        