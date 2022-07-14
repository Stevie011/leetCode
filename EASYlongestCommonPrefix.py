class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #this is just to find the min length of the strings to run the loop the least amount of times
        lengths = []
        #loop thru strs
        for i in strs:
            #add length of each to array
            lengths.append(len(i))
        #find the min of the lengths
        minLen = min(lengths)
        #empty string for prefix
        tempPrefix = ""
        #loop, limited to length of shortest word
        for i in range(minLen):
            #each loop, add the next letter of the 1st word to tempPrefix
            tempPrefix += strs[0][i]
            #go through each word in strs
            for j in range(len(strs)):
                #slice that word to the same length as tempPrefix, if it doesn't equal temp prefix:
                if strs[j][0:len(tempPrefix)] != tempPrefix:
                    #return tempPrefix with the last letter chopped off
                    return tempPrefix[:len(tempPrefix)-1]
        return tempPrefix
            
        