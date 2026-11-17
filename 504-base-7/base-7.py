class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num<0:
            a = "-"
        else:
            a = ""
        num = abs(num)
        b = ""
        while num:
            b = str(num % 7)+b
            num //= 7
        return a+b