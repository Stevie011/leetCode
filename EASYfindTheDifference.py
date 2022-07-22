class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lt = list(t)
        for i in s:
            lt.remove(i)
        return lt[0]
        
        