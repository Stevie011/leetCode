class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #fringe case 1
        if n==1: return True
        count = 1
        # if its not a power of 2, count wont equal n (it'll be one off)
        while count < n:
            count *= 2
        return count == n
        