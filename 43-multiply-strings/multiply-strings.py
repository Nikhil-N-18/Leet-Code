class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m=len(num1)
        n=len(num2)
        res = [0]*(m+n)
        for i in range(m-1,-1,-1):
            a = int(num1[i])
            for j in range(n-1,-1,-1):
                b = int(num2[j])
                c = a*b
                p1 = i+j
                p2 = i+j+1
                full = c + res[p2]
                res[p2] = full % 10
                res[p1] += full // 10
        sub = ""
        for k in res:
            if not (len(sub) == 0 and k==0):
                sub += str(k)
        return sub if sub else "0"
