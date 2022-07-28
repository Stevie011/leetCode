class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #empty answer array
        ansArr =[]
        #min occurences, as per question
        minOcc = len(nums)//3
        #remove dups to improve runtime
        numSet = set(nums)
        #loop thru shorter set
        for i in numSet:
            #check if i occurs more times than min
            if nums.count(i) > minOcc:
                #if it does, add it to the ansArr
                ansArr.append(i)
        #sing it back
        return ansArr

            
        
        