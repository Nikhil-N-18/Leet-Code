class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        a = lambda s: sum(days[:int(s[:2])-1]) + int(s[3:])
        a1,a2 = a(arriveAlice),a(leaveAlice)
        b1,b2 = a(arriveBob),a(leaveBob)
        return max(0,min(a2,b2)-max(a1,b1)+1)