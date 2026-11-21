class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = float('inf')
        sum1 = 0
        for i in prices:
            if i < n:
                n = i
            else:
                sum1 = max(sum1,i-n)
        return sum1