class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numsDict = {"0": 0, "1": 1, "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        return str(int("".join([str(numsDict[i]) for i in num1])) * int("".join([str(numsDict[i]) for i in num2])))
        