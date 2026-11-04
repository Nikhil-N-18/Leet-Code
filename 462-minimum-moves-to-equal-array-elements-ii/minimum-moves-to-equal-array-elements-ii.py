import math
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)//2
        median = nums[n]
        sum1 =  0
        for i in range(len(nums)):
            sum1 += abs(nums[i]-median)
        return int(sum1)