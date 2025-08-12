"""
Title     : Ways to Express an Integer as Sum of Powers
Difficulty: Medium

Given two positive integers n and x.
Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.
Since the result can be very large, return it modulo 109 + 7.
For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.
 
Example 1:

Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.

Example 2:

Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.

 
Constraints:

1 <= n <= 300
1 <= x <= 5
"""

# Your solution below:
To solve this problem, we can use dynamic programming (DP). We generate an auxiliary 2D array dp[n + 1][j + 1], where dp[i][j] stores the number of ways we can express i as the sum of the xth power of unique integers from 1 to j.

At the initial stage, we set dp[0][0] to 1 since there is exactly 1 way to represent number 0, i.e., by using no integers. All other dp[i][0], where i >= 1, are set to 0 as it's impossible to represent a positive number using no integers.

For every j >= 1, we calculate dp[i][j] in two ways:

    Consider the jth integer in the set: If j^x is less than or equal to i, then the number of ways to represent i would be the number of ways to represent (i - j^x) using integers from 1 to j (dp[i - j**x][j]).

    Not consider the jth integer in the set: In this case, the number of ways would be number of ways to represent i using integers from 1 to (j - 1) (dp[i][j - 1]).

The final answer will be stored at dp[n][j] as it counts the total number of ways to represent number n using all positive integers from 1 to j, where j^x is less than or equal to n.

Here is the Python solution:

```python
MOD = 10**9 + 7
def sumPowers(n: int, x: int) -> int:
    # Store all j**x in an array till it is less than or equal to n 
    # to avoid same exponential calculation again and again.
    arr = [j**x for j in range(1, n+1) if j**x <= n]
    
    # Initialize the dp array
    dp = [[0]*len(arr) for _ in range(n+1)]
    dp[0][0] = 1
    
    # Build the dp array
    for i in range(n+1):
        for j in range(1, len(arr)):
            dp[i][j] += dp[i][j-1]  # Not consider the jth integer
            if i >= arr[j]:  # Consider the jth integer
                dp[i][j] += dp[i - arr[j]][j-1]
                dp[i][j] %= MOD
    
    return dp[-1][-1]
```
This solution has time complexity O(n^2) and space complexity O(n^2).
