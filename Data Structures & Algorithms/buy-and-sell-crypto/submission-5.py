class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if(n == 1):
            return 0
        l, r = 0,1
        maxValue = 0
        while(r < n):
            profit = prices[r]-prices[l]
            if(profit < 0):
                l=r
            elif(profit > maxValue):
                maxValue = profit
            r+=1
        return maxValue