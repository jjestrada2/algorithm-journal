class Solution:
    """
    Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
 

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
    """
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls > lt :
            return self.isOneEditDistance(t,s)
        

        for i in range(ls):
            if s[i] != t[i]:
                if ls == lt:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]

        return ls + 1 == lt
    

sol = Solution()
print("abc & ab")
print(sol.isOneEditDistance("abc","ab"))