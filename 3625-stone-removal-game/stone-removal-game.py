class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        a = n-10
        for i in range(9,-1,-1):
            if a<i:
                return i % 2 ==1
            a = a-i
        return False