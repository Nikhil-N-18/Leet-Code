class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        pre = ""
        for i in range(len(strs[0])):
            a = strs[0][i]
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=a:
                    return pre
            pre += a
        return pre