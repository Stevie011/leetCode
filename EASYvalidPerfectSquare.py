class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #square root it (**0.5), use int() to chop off fraction, if its perfect square it won't have a fraction
        return (num ** 0.5) == int(num ** 0.5)
        