class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #this is gross
        if len(nums) ==1 and nums[0] ==0:
            return 1
        elif len(nums) ==1 and nums[0]==1:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif list(set([i for i in range(1,len(nums)+1)]).difference(set(nums))):
            return list(set([i for i in range(1,len(nums)+1)]).difference(set(nums)))[0]
        else:
            return 0