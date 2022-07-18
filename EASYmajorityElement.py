# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         majorCand = nums[0]
#         count=1
#         for i in range(1,len(nums)):
#             if nums[i] == majorCand:
#                 count +=1
#             else:
#                 count -= 1
#             if count == 0:
#                 majorCand = nums[i]
#                 count = 1
#         return majorCand

#apparently sort() is an inefficient choice but this is so much neater--

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
            
        
            
        