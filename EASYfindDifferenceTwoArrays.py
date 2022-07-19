class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #use list comprehension to return new list - loop through nums1 =, add i to new list if i not in nums2, swap for other list. use list(set( to remove dups
        return [list(set([i for i in nums1 if i not in nums2])),list(set([i for i in nums2 if i not in nums1]))]
        