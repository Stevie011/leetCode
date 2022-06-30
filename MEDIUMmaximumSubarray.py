class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #sliding window style --linear time complexity
        
        #set ansNm to first element of array- if array length is 1, it'll return the same 1
        ansSum = nums[0]
        #temp variable for current "sliding window" sum
        tempSum = 0
        #standard loop through nums
        for i in nums:
            #each loop, if tempSum is negative (coz then it can't be the winner) set it back to 0
            #tempSum represents numbers added to this point
            #if its resulted in a negative number, we only want to check to the right of the array, because it's
            #better to start a new subarray (same as starting at 0)
            if tempSum < 0:
                tempSum = 0
            #if it's a positive number, add i, coz it might be the new largest sub array
            tempSum += i
            #each loop, check if this temp sum is the new biggest sum we've seen
            #max() returns max of inputted values
            ansSum = max(ansSum, tempSum)
        #spits out the biggest one yet
        return ansSum
            
        
        