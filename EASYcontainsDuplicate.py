class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(list(nums)) != len(dict.fromkeys(list(nums))) else False
