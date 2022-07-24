class Solution:
    def reverseWords(self, s: str) -> str:
        #splat- past tense of split(jk not really)
        #split s into component words
        splat = s.split(" ")
        #empty new array
        newArr = []
        #loop thru split list, add each word reversed 
        for i in range(len(splat)):
            newArr.append(splat[i][::-1])
        #join them with spaces for the return
        return " ".join(newArr)

        #same idea in one line    
        #return " ".join([x[::-1] for x in list(s.split())])
