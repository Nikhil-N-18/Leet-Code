class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map1 = {0:-1}
        sum=0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sum-=1
            else:
                sum += 1
            if sum in map1:
                maxi = max(maxi,i-map1[sum])
            else:
                map1[sum] = i
        return maxi