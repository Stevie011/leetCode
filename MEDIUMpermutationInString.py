class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window slice
        sort1 =  "".join(sorted(s1))
        for i in range(0, len(s2)-len(s1)+1):
            if sort1 == "".join(sorted(s2[i:i+len(s1)])):
                return True
        return False
        