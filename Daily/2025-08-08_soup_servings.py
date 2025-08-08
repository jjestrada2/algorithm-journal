"""
Title     : Soup Servings
Difficulty: Medium

You have two soups, A and B, each starting with n mL. On every turn, one of the following four serving operations is chosen at random, each with probability 0.25 independent of all previous turns:

pour 100 mL from type A and 0 mL from type B
pour 75 mL from type A and 25 mL from type B
pour 50 mL from type A and 50 mL from type B
pour 25 mL from type A and 75 mL from type B

Note:

There is no operation that pours 0 mL from A and 100 mL from B.
The amounts from A and B are poured simultaneously during the turn.
If an operation asks you to pour more than you have left of a soup, pour all that remains of that soup.

The process stops immediately after any turn in which one of the soups is used up.
Return the probability that A is used up before B, plus half the probability that both soups are used up in the same turn. Answers within 10-5 of the actual answer will be accepted.
 
Example 1:

Input: n = 50
Output: 0.62500
Explanation: 
If we perform either of the first two serving operations, soup A will become empty first.
If we perform the third operation, A and B will become empty at the same time.
If we perform the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Example 2:

Input: n = 100
Output: 0.71875
Explanation: 
If we perform the first serving operation, soup A will become empty first.
If we perform the second serving operations, A will become empty on performing operation [1, 2, 3], and both A and B become empty on performing operation 4.
If we perform the third operation, A will become empty on performing operation [1, 2], and both A and B become empty on performing operation 3.
If we perform the fourth operation, A will become empty on performing operation 1, and both A and B become empty on performing operation 2.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.71875.

 
Constraints:

0 <= n <= 109
"""

# Your solution below:
A dynamic programming approach can be used to solve this problem. We use a 2D array dp[i][j] to record the probability that soup A becomes empty when there are i ml left in soup A and j ml left in soup B. The detailed steps are as follows:

1. Initialization: dp[0][0] = 0.5, which represents the probability that both A and B become empty at the same time; and for any j>0, dp[0][j] = 1.0, which represents the probability that A becomes empty before B.

2. Transition: For any i, j such that i+j>0, we try all four possible serving operations, and add up their probabilities according to the rule:

    dp[i][j] = 0.25 * (dp[max(0, i-100)][j] + dp[max(0, i-75)][max(0, j-25)] + dp[max(0, i-50)][max(0, j-50)] + dp[max(0, i-25)][max(0, j-75)])

3. Finally, return dp[n][n] as the result.

Python code:

```python
class Solution:
    def soupServings(self, N: int) -> float:
        if N >= 4800: # if N is large enough, it's almost certain that A becomes empty before B.
            return 1.0
        
        N = (N + 24) // 25 # round up and scale down to avoid floating-point errors.
        dp = [[0.0 for _ in range(N+1)] for _ in range(N+1)]
        dp[0][0] = 0.5
        for j in range(1, N+1):  # when A becomes empty before B.
            dp[0][j] = 1.0

        for i in range(1, N+1):
            for j in range(N+1):
                dp[i][j] = 0.25*(dp[max(0, i-4)][j] if i>=4 else 0.0 +
                            dp[max(0, i-3)][max(0, j-1)] if i>=3 and j>=1 else 0.0 +
                            dp[max(0, i-2)][max(0, j-2)] if i>=2 and j>=2 else 0.0 +
                            dp[max(0, i-1)][max(0, j-3)] if i>=1 and j>=3 else 0.0)

        return dp[N][N]
```

This solution is very efficient with time complexity of O(n^2) and space complexity of O(n^2).
