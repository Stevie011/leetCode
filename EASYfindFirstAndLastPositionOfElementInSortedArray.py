class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #start ans arr like this, def val if target not found
        ansArr = [-1,-1]
        # 2 pointers setup
        l,r= 0, len(nums)-1
        #might be able to opotimise it my limiting loop differently
        while l < len(nums):
            #only change ansarr for first value (all other vals will be > 0)
            if ansArr[0] < 0 and nums[l] == target:
                ansArr[0] = l
            if ansArr[1] < 0 and nums[r] == target:
                ansArr[1]=r
            #bring pointers in together
            l+=1
            r-=1
        return ansArr
