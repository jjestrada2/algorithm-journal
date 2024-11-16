class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"(":")","{":"}","[":"]"}
        stk = []
        for i in range(len(s)):
            if s[i] in mp:
                stk.append(mp[s[i]])
            elif len(stk) == 0 or stk.pop() != s[i]:
                return False
        return len(stk) == 0
    
sol = Solution()
print("{([])}")
print( sol.isValid("{([])}"))