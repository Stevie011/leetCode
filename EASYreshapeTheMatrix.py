class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        #length of first entry in matrix
        firstLen= len(mat[0])
        #length of total mat
        matLen = len(mat)
        #work out no of required entries in answer matrix
        totalReqEnts = r*c
        #check if new matrix is possible with requirements
        if firstLen*matLen != totalReqEnts:
            #if not, return og mat
            return mat
        #first loop for columns, second for rows
        #how with dict comp???
        ansArr = [[0 for _ in range(c)]for _ in range(r)]

        #ansArr = []


        #empty temp arr
        tempArr =[]
        #enter all values of og arr into new arr
        for i in range(matLen):
            for j in range(firstLen):
                tempArr.append(mat[i][j])

        #new counter variable
        k=0
        #loop through rows
        for i in range(r):
            #loop through columns
            for j in range(c):
                #add bits of tempArr 1 by 1
                ansArr[i][j] = tempArr[k]
                #go to next element of tempArr
                k +=1

        return ansArr
        