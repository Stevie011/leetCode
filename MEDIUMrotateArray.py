class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #slow but super simple
        #loop as many times as k
        for i in range(k):
            #insert the last item at the beginning of nums
            nums.insert(0, nums[-1])
            #pop the last one off the end
            nums.pop(-1)
        #sing it back
        return nums
            
        