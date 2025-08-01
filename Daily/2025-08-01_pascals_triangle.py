"""
Title     : Pascal's Triangle
Difficulty: Easy

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]

 
Constraints:

1 <= numRows <= 30
"""

# Your solution below:
Solution:

Here is the Python code to generate the first numRows of Pascal's Triangle:

```python
def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal
```
This script first constructs a list of lists where each sub-list has a length corresponding to its level in the triangle. It has prepopulated all these lists with 1's because the first and last elements of all rows are always 1.

For example, if numRows = 5 the `pascal` list will initially look like this `[[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]`.

Then it iterates over each element of each row in the triangle that lies in-between the first and last element. For each of these elements, it calculates the value as the sum of the two values above it. This is done using the equation `pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]` where `i` is the row number and `j` is the column number.

For example, in the 4th row `3 = 1 (from the third row, second column) + 2 (from the third row, third column)`.

This process is repeated up to the given numRows, and then the solution is returned.

For numRows = 5, the final `pascal` will look like this `[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]`.

The time complexity of the solution is O(n^2) where n is the numRows because there are two nested loops in the code. The space complexity is also O(n^2) because we are storing the computed triangle up to n rows and each row has nearly n items for a large row.
