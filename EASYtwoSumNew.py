class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #standard nested loops
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        #loops starting from opposite ends
                
         for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                if nums[i] + nums[j] == target:
                    return [i,j]
        
        