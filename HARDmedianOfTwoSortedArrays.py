class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #merge and sort both arrays
        merge = sorted(nums1 + nums2)
        #find middle point
        mid = float(len(merge))/2
        #if list length is odd
        if len(merge)%2 != 0:
            #return center element
            return merge[int(mid - 0.5)] 
        #if merge list len is even
        else:
            #return sum of mid 2 / 2
            return (merge[int(mid-1)] + merge[int(mid)])/2
        #if else statement in ternary form for the lolz
        #return merge[int(mid - 0.5)] if len(merge)%2 != 0 else (merge[int(mid-1)] + merge[int(mid)])/2
        