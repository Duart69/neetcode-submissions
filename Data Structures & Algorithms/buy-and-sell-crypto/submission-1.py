class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minArray = [float('inf')]*n
        maxArray = [float('-inf')]*n
        for i in range(1,n):
            minArray[i] = min(prices[i-1], minArray[i-1])
        maxArray[n-1] = prices[n-1]
        for i in range(n-2,-1,-1):
            maxArray[i] = max(prices[i], maxArray[i+1])
        profit = 0
        for i in range(n):
            if(maxArray[i]-minArray[i]>profit):
                profit = maxArray[i]-minArray[i]
        return profit