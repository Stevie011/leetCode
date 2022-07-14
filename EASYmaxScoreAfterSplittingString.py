class Solution:
    def maxScore(self, s: str) -> int:
        #empty int for max score
        maxNo = 0
        #loop for each iterm in string but shift it forward by 1 (coz each side must be non zero)
        for i in range(1, len(s)+1):
            #split string to either side of i 
            left = s[:i]
            right = s[i:]
            #count 0 and 1 in each
            leftNum = left.count("0")
            rightNum = right.count("1")
            #if the length of either side is zero or less break
            if len(left) <= 0 or len(right) <= 0:
                 break
            #else compare sum of left and right with previous max, keep max
            maxNo = max(leftNum + rightNum, maxNo)
        #bring him home
        return maxNo

       
        