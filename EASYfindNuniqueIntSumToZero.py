class Solution:
    def sumZero(self, n: int) -> List[int]:
        # remaining = n
        # i=0
        # j=1
        # result = []
        # while i<n and remaining>1:
        #     result.append(j)
        #     result.append(-j)
        #     remaining -= 2
        #     i += 2
        #     j+=1
        # if remaining ==1:
        #     result.append(0)
        # return result
        if n==1: return [0]
        if n==2: return [-1,1]
        
        ansArr=[]
        
        for i in range(n-1):
            ansArr.append(i)
        ansArr.append(-sum(ansArr))
        
        return ansArr
        