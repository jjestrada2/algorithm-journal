"""
Title     : Count Square Submatrices with All Ones
Difficulty: Medium

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
 
Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

 
Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""

# Your solution below:
Sure, this problem can be solved by using dynamic programming concept as follows:

Algorithm Explanation
1. If the value in the cell of the matrix is 1, then the size of biggest square that includes that cell as the right bottom cell would be min(the size of biggest square ending at cell above, the size of biggest square ending at cell to the left, the size of biggest square ending at cell to the left top) + 1. Else if the cell value is 0, then it can't be a part of a square and so, square size would be 0.
2. Track the sum of the sizes calculated in the previous step for all cells and return, this acts as the count of square submatrices with all ones.

Here's the Python code that implements the above algorithm:

```python
def countSquares(matrix):
    if not matrix: return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0]*n for _ in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = matrix[i][j]
            elif matrix[i][j]:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
            count += dp[i][j]
    return count
```

In the above code, `dp` is the dynamic programming table that stores the maximum size of the square that includes the cell under consideration. We traverse through the input matrix and update the `dp` table accordingly. Finally, the sum of all the cells in the `dp` table will be the count of square submatrices with all ones.

For example:

For the matrix 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Step 1: `dp` table after the first iteration
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Step 2: `dp` table after the second iteration
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Step 3: `dp` table after the third iteration
[
  [1,0,1],
  [1,1,1],
  [1,1,1]
]
Step 4: Count of square submatrices = sum of elements in `dp` = 7
