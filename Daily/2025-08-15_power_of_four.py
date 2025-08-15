"""
Title     : Power of Four
Difficulty: Easy

Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
 
Example 1:
Input: n = 16
Output: true
Example 2:
Input: n = 5
Output: false
Example 3:
Input: n = 1
Output: true

 
Constraints:

-231 <= n <= 231 - 1

 
Follow up: Could you solve it without loops/recursion?
"""

# Your solution below:
The logic behind checking if a number is a power of 4 is relatively straightforward. 

- First, we check if the input number is less than or equal to zero, in which case the function returns False since zero and negative numbers cannot be powers of 4.

- Next, we calculate the binary logarithm of the number and store the result in a variable. 

- If the input number was a power of 4, the result of this logarithmic operation should be an integer. This works because a power of 4 essentially means that the input number can be expressed as 4 raised to some integer power, or in other words the base-2 logarithm of that number should be an even number.

- We can check this by comparing the result of the logarithmic operation to its equivalent as an integer. If the two numbers are the same, this means that the logarithm is an integer value, and thus the original input number is a power of 4.

- In Python, the `log` function from the math module can be used to compute the base-2 logarithm, and the `int` function is used to remove any decimal points from a number.

Here's the Python code implementing this logic:

```python
import math

def isPowerOfFour(n: int) -> bool:
    if n <= 0:
        return False
    log = math.log(n, 4)
    return log == int(log)
```

For the follow-up, a number that's a power of 4 would have a binary representation that starts with a 1 followed by an even number of 0s. If the number `n` is positive and only one bit is set in the binary representation of `n`, it is a power of 2. In a 32-bit signed integer, for a number `n` to be power of 4, it has to be power of 2 and the count of zero bits following the only set bit in `n` has to be even.

So, the following python code does it without loops/recursion:

```python
def isPowerOfFour(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
``` 

In this line of Python code `(n & (n - 1)) == 0` checks if there is only one bit that is set to 1. And `(n & 0x55555555) != 0` checks if there are even zero bits following the set bit. Here, `0x55555555` is a 32 bit number with even bits set to 1 i.e., it is 1010101010101010101010101010101 in binary.
