 class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #slow as hell, find some way to optimise
        maxCount=0
        counter=0
        tempArr =[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] in tempArr:
                    break
                else:
                    tempArr.append(s[j])
                    counter+=1
                
            maxCount = max(maxCount, counter)
            counter=0
            tempArr=[]
        return maxCount
                
        