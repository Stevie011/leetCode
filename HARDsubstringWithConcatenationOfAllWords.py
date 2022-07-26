class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        #join words together, find length of total 
        lenWords = len("".join(words))
        #empty array
        ansArr =[]
        
        #loop thru words- skip last bit, coz words can't fit if len of rem string is less than words
        for i in range((len(s)-lenWords)+1):
            #clumsy chunking method
            #don't think i need to change it to string first
            str = s[i:i+lenWords]
            n= len(words[0])
            chunk = [str[i:i+n] for i in range(0, len(str), n)]
            #new empty array
            tempArr = []
            #loop thru words
            for j in words:
                #if the word is not in chunk
                if j not in chunk:
                    #clear the temp array
                    tempArr.clear()
                    #next iteration (all words must be in chunk)
                    break
                #add i to tempArr once only
                if j in chunk and len(tempArr) <1:
                    tempArr.append(i)
                    #remove j (to check for dups)
                    chunk.remove(j)
                #no point adding i to temp arr again
                elif j in chunk and len(tempArr) >=1:
                    #just remove the chunk
                    chunk.remove(j)
            
            if len(tempArr)>0:           
                ansArr.append(tempArr[0]) 
        return ansArr
                    
                
        