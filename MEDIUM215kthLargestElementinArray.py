class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #sort the list
        nums.sort()
        #kth largest so we count from the right  - negative number
        return nums[(-k)] 