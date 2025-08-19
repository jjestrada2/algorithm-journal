"""
Title     : Number of Zero-Filled Subarrays
Difficulty: Medium

Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array.
 
Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

Example 3:

Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.

 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# Your solution below:
Sure, Here is a Python solution.

The idea behind this solution is to keep track of the lengths of continuous sequences of zeros in the input list. We can achieve this using a variable 'cnt' initialized to 0 which gets incremented whenever we encounter a zero and reset to 0 for non-zero elements. We use another variable 'res' to record the total count of zero-filled sub-arrays. This is computed by adding the triangular number of 'cnt' to 'res' every time 'cnt' is reset (which is when we encounter a non-zero element after a sequence of zeros).

```python

def countZeroSubArrays(nums):
    cnt, res = 0, 0
    for num in nums:
        if num == 0:
            cnt += 1
        else:
            # when we encounter a non-zero after a sequence of zeros,
            # add the triangular number of the count of zeros to the result
            res += cnt*(cnt + 1) // 2
            cnt = 0
    # for the case where the array ends with one or more zeros,
    # we add the remaining count of zeros to the result
    res += cnt * (cnt + 1) // 2
    return res

```

Let's test it for all the example inputs

```python
print(countZeroSubArrays([1,3,0,0,2,0,0,4])) # should print 6
print(countZeroSubArrays([0,0,0,2,0,0])) # should print 9
print(countZeroSubArrays([2,10,2019])) # should print 0
```

The time complexity of this code is O(n), where n is the length of the input list, since we make a single pass through the array. The space complexity is O(1), as we do not use any additional space that scales with the input size.
