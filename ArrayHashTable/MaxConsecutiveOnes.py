from typing import List

class Solution:
    """
    Problem:
    Given a binary array nums, return the maximum number of consecutive 1's in the array.

    Example:
    Input: nums = [1, 1, 0, 1, 1, 1]
    Output: 3
    Explanation: The first two digits and the last three digits have consecutive 1s.
                 The maximum number of consecutive 1s is 3.
    """
    
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 0
        return maxCount

# Test the function
if __name__ == "__main__":
    solution = Solution()
    test_nums = [1, 1, 0, 1, 1, 1]
    result = solution.findMaxConsecutiveOnes(test_nums)
    print(f"The maximum number of consecutive ones is: {result}")
