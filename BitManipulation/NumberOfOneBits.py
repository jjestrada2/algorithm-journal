class Solution:
    """
    Given a positive integer n, write a function that returns the number of 
set bits
 in its binary representation (also known as the Hamming weight)."""
    def hammingWeight(self, n: int) -> int:
        i = 0
        while n > 0:
            i += 1
            print(bin(n) +'  &  '+ bin(n-1) + ' = ')
            n = (n-1) & n
            print(bin(n)+'\n')

        return i
    

sol = Solution()
ans = sol.hammingWeight(11)
print(ans)