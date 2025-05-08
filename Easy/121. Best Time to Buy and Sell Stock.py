class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m=prices[0]
        profit=0
        
        for p in prices[1:]:
            if p<m:
                m=p
            else:
                profit=max(profit,p-m)
        return profit
