class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for i in arr1:
            ans = True
            for j in arr2:
                if abs(i-j)<=d:
                    ans = False
                    break
            if ans:
                count += 1
        return count