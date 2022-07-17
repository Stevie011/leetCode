class Solution:
    def reverse(self, x: int) -> int:
        
        ansStr = ""
        emptyList = []
        strNum = str(x)
        for i in strNum:
            emptyList.append(i)
        if emptyList[0] == "-":
            ansStr += "-"
            emptyList.pop(0)
        revList = "".join(emptyList[::-1])
        ansInt = int(ansStr + revList)
        if ansInt < -2**31 or ansInt > (2**31)-1:
            return 0
        else:
            return ansInt
      
        
            