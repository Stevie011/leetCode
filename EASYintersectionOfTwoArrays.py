class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #count no of occurences to avoid duplicates
        count = Counter(nums1)
        #empty answer list
        ansList = []
        #go through other list
        for i in nums2:
            #checks if item present in count
            if count[i] > 0:
                #add it to answer list
                ansList.append(i)
                #decrease count to make sure item is added once per (avoid dups)
                count[i] -= 1
        #bring him home
        return ansList
        