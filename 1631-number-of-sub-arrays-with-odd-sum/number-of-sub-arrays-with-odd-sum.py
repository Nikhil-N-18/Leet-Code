class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        sum1 = 0
        odds = 0
        for i in range(len(arr)):
            sum1 += arr[i]
            odds += sum1 % 2
        odds += (len(arr)-odds)*odds
        return int(odds%1000000007)