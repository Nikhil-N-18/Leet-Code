class Solution:
    def checkString(self, s: str) -> bool:
        a = False
        for i in s:
            if i=="b":
                a = True
            if i == 'a' and a:
                return False
        return True