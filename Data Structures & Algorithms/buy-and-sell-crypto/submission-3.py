class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        profit = 0
        if len(prices)<=1:
            return profit
        while l<r:

            if prices[l]>prices[r]:
                l=r
                # r+=1
            
            if prices[r]>prices[l] and prices[r]-prices[l]>profit:
                profit = prices[r]-prices[l]
            r+=1
            if r==len(prices):
                break
        return profit

                