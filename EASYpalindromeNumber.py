class Solution:
    def isPalindrome(self, x: int) -> bool:
        #convert int to str, check if it's the same as itself reversed
        return str(x) == str(x)[::-1]
        