class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #there has to be a better way of doing this
        #counter, coz the unit tester wants k 
        k = 0
        #empty list
        checkList = []
        #go through nums
        for i in nums:
            #if i isn't already in check list
            if i not in checkList:
                #add it now
                checkList.append(i)
        #clear put the whole of nums
        nums.clear()
        #add each item in the checkList back into nums and increase counter by 1
        for i in checkList:
            nums.append(i)
            k+=1
        #spit the count out
        return k
        