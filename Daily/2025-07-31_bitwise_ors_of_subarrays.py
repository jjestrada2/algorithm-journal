"""
Title     : Bitwise ORs of Subarrays
Difficulty: Medium

Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.
The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.
A subarray is a contiguous non-empty sequence of elements within an array.
 
Example 1:

Input: arr = [0]
Output: 1
Explanation: There is only one possible result: 0.

Example 2:

Input: arr = [1,1,2]
Output: 3
Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.

Example 3:

Input: arr = [1,2,4]
Output: 6
Explanation: The possible results are 1, 2, 3, 4, 6, and 7.

 
Constraints:

1 <= arr.length <= 5 * 104
0 <= arr[i] <= 109
"""

# Your solution below:
A python solution for this problem is to keep track of a set of ORs for each element in the array. The key observation here is that only the ORs that include the most recent element matter so we don't need to iterate over all possible subarrays, just the ones that end with the current element.

Here's a python solution:

```python
def subarrayBitwiseORs(arr):
    ans = set()
    cur = {0}
    for i in arr:
        cur = {i | j for j in cur}  | {i}
        ans |= cur
    return len(ans)
```
In the above Python code:
- The variable `ans` is used to store the unique OR results for all subarrays.
- The variable `cur` stores the OR results for subarrays ending at the current index.
- For each element in the array, we update `cur` to reflect the OR results of all subarrays ending at the new element.
- For every new element, we calculate OR with the previous elements and include a set with only current element itself. "|" is used to get a union of sets.
- We calculate the union of `ans` and `cur` to update `ans`.
- Finally, we return the size of the `ans`, i.e., the number of distinct bitwise ORs of all the non-empty subarrays of arr. 

This solution runs in O(n) time complexity where n is the number of elements in the input array and requires O(n) auxiliary space. 

Let's try with some inputs:

```python
# Input 1
print(subarrayBitwiseORs([0]))  # Output: 1
# Input 2
print(subarrayBitwiseORs([1,1,2]))  # Output: 3
# Input 3
print(subarrayBitwiseORs([1,2,4]))  # Output: 6
```
