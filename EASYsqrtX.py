class Solution:
    def mySqrt(self, x: int) -> int:
        #this is not ideal
        #fringe cases 0,1,2
        if x == 0:
            return 0
        elif x==1 or x==2:
            return 1
        else:
            #else loop through numbers, check if valid square, if exceeds limit return previous i
            for i in range(x):
                if i*i == x:
                    return i
                elif i*i > x:
                    return i-1
        