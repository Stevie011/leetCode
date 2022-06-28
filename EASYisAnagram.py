class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if sorted string s is the same as sorted string t
        return True if sorted(s)==sorted(t) else False

        