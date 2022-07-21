class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #standard binary search format
        l,r = 0, len(nums)-1
    
        while l <= r:
            m = (l+r)//2
            if target==nums[m]:
                return m
            if nums[m] < target:
                l = m+1
            else:
                r = m-1
        #if target not found return left pointer (that would be the insert postion)
        return l
