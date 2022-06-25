class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #empty answer list
        ansList = []
        #loop till specified number
        for i in range(numRows):
            ansList.append([])
            #put in a 1
            ansList[i].append(1)
            #next loop
            for j in range(1, i):
                #here's the maffs
                ansList[i].append(ansList[i-1][j-1]+ansList[i-1][j])
            #only need to add 1 once if there's no more rows
            if i > 0:
                ansList[i].append(1)
                
        return ansList
                
        