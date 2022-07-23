class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #start left and roght pointer on either side
        l,r = 0, len(numbers)-1
        #stop loop when pointers meet
        while l<r:
            #if the sum matches target, return the indices (dont forget to add 1)
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            #if bigger, shift right pointer
            elif numbers[l] + numbers[r] > target:
                r -=1
            #else shift left
            else:
                l +=1
            