import math
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            pro = 1
            val1 = 0
            val2 = 1
            for j in range(i,n):
                pro *= nums[j]
                val1 = math.gcd(val1,nums[j])
                val2 = math.lcm(val2,nums[j])
                if pro == val2*val1:
                    ans = max(ans,j-i+1)
        return ans