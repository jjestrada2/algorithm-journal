"""
Title     : Power of Two
Difficulty: Easy

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
 
Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

 
Constraints:

-231 <= n <= 231 - 1

 
Follow up: Could you solve it without loops/recursion?
"""

# Your solution below:
Here is the Python solution for the problem:

```python
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0
```
Explanation:
The solution is using bitwise operations to solve this question. For a number to be a power of two, it should only have one '1' bit in its binary representation. The bitwise AND operation between n and (n - 1) would make the rightmost 'set' bit in n to 0 and all the rest bits of (n - 1) and n are the same. So if the result is 0, there is only one 'set' bit in n, which means that n could be present as 2^x, where x is a nonnegative integer, so n is a power of 2. At the same time, since the power of 2 cannot be a negative number or zero, we check n > 0 in the return statement as well.
