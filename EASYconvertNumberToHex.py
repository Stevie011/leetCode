class Solution:
    def toHex(self, num: int) -> str:
        #empty list for answer
        ansList=[]
        #dict for vals that need to be converted
        hexDict = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        #if num is 0 we can just spit 0 straight out
        if num==0:
            return "0"
        #cover for negative numbers formula
        if num <0:
            num = num + 2**32
        #stop the loop when num hits 0
        while num>0:
            #get remainder using modulo
            rem = num%16
            #get quotient (before decimals) using //
            num = num//16
            #if remainder is btwn 9 and 16, we know it must be converted using dict
            if rem > 9 and rem < 16:
                rem = hexDict[rem]
            #else we can can just convert it to string
            else:
                rem = str(rem)
            #add it to the answer list
            ansList.append(rem)
        #join the answer list and reverse the order
        return "".join(ansList[::-1])