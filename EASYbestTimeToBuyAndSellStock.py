class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        buyPoint = 0
        sellPoint = 1
        maxProfit = 0
        
        while sellPoint < len(prices):
            #check if current iteration would give higher profit
            if prices[buyPoint] < prices[sellPoint]:
                # calc current profit
                currentProfit = prices[sellPoint] - prices[buyPoint]
                #check if more profitable than old max
                maxProfit = max(maxProfit, currentProfit )
            else:
                #shift it all the way to the right, because it must be best buy point
                buyPoint = sellPoint
            sellPoint +=1
            
        return maxProfit
        
      
            