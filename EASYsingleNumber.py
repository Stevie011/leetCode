class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #what's a better way to do this?
        #empty answer list
        ansList = []
        #loop thru nums
        for i in nums:
            #if i is slready in list, remove it
            if i in ansList:
                ansList.remove(i)
            #else add it
            else:    
                ansList.append(i)
        #return first (and only) element of answer list
        return ansList[0]
        