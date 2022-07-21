class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #for loop is much quicker than 1 liner
        # for i in range(0, len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        
        #slow one liner
        #return nums.index(target) if target in nums else -1
        
        #binary search
        l = 0
        r = len(nums)-1
        m = 0
        
        while l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m
        return -1
            