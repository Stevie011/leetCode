class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        #list comp to get elements of int into list
        splat = [i for i in str(n)]
        #product variable
        product = 1
        #mult each element in list  NB start at 1 not 0 (0 * anything is 0)
        for i in splat:
            product *= int(i)
        #sum var      NB sum is reserved name
        _sum=0
        #add each element in list
        for i in splat:
            _sum += int(i)
        #return difference
        return product - _sum
        