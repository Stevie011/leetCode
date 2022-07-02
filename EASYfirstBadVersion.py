# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #bisection search
        
        low = 1
        high = n
        mid = (low+high)//2
        
        while low <= high:
            #if it's the first one bring it home
            if isBadVersion(mid) and (mid ==1 or not isBadVersion(mid-1)):
                return int(mid)
            #if there are more before mid change end position
            elif isBadVersion(mid) and isBadVersion(mid-1):
                high= mid-1
            else:
                #move low point forward
                low = mid+1
            mid = (low+high)//2
        #return this if condition never met
        return -1
        
    
                