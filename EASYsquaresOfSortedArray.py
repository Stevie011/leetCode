class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # ansArr = [i**2 for i in nums]
        # ansArr.sort()
        # return ansArr
        
        # same idea in one line
        return sorted([i**2 for i in nums])
        