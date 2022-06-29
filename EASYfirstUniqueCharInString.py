class Solution:
    def firstUniqChar(self, s: str) -> int:
        #empty dictionary
        mapDict = {}
        #loop through string 
        for i in s:
            #if char not already in dict, adds it in, sets value as true
            if i not in mapDict:
                #set its value to true
                mapDict[i] = True
            #if it's a dup, change value to false
            else:
                mapDict[i] = False
        #enumerate with 2 vals coz we need to return index
        #research enumerate more
        for j,k in enumerate(s):
            #if val is present in dict, it'll return the 1st one it hits
            if mapDict[k]:
                return j
        #else return -1 if val not present
        return -1
        