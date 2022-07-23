class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                j=i+1
                while j < length:
                    if nums[j] != 0:
                        temp = nums[i]
                        nums[i]=nums[j]
                        nums[j]=temp
                        break
                    j+=1
        