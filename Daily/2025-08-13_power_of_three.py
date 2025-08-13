"""
Title     : Power of Three
Difficulty: Easy

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
 
Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33

Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).

 
Constraints:

-231 <= n <= 231 - 1

 
Follow up: Could you solve it without loops/recursion?
"""

# Your solution below:
In python you can solve this problem by continuously dividing the given number by 3 until we can no longer do so cleanly (i.e., without a remainder), at which point we should be left with a 1 if the number is a power of 3.

Here's how you can do it in Python:

```python
def isPowerOfThree(n):
    if n > 1:
        while n % 3 == 0:
            n /= 3
    return n == 1
```

We first check if the given number is greater than 1 (since 3 to the power of anything is always greater than 1), and if it is, we begin a loop in which we divide the number by 3 as long as we can do so exactly, which means it is a power of three. When we can no longer divide by 3 without leaving a remainder, we check if we're left with a 1, which we should be if the original number was a power of 3.

This solution is very efficient and runs in O(log n) time complexity because in the worst case we divide the given number n by 3 in each iteration of the loop. This loop will terminate once we have reduced n down to 1, which will take log base 3 of n iterations. Thus, the time complexity of this solution is O(log n).

Regarding follow-up, we could solve it without loops or recursion by using mathematics. The largest power of three which fit in an integer is 3^19 = 1162261467, which is a power of three. Every other power of 3 (3^0, 3^1, etc.) up to 3^19 will divide 1162261467 evenly, so we can simply return 1162261467 % n == 0 to determine whether n is a power of 3:

```python
def isPowerOfThree(n):
    return n > 0 and 1162261467 % n == 0
```

In this solution, we take the advantage of number 1162261467 (3 to the power of 19) being the maximum possible power of 3 that fits in the 4-byte signed integer. If n is greater than this value, we should return false. If it is less than or equal to this value, we return true only if the modulus is 0 (i.e., 1162261467 is divisible by n). This one-liner solution runs in constant, O(1) time.
