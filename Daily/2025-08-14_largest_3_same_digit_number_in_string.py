"""
Title     : Largest 3-Same-Digit Number in String
Difficulty: Easy

You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.
Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.

 
Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.

Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

 
Constraints:

3 <= num.length <= 1000
num only consists of digits.
"""

# Your solution below:
Here's how you can approach this problem:

To solve for the maximum good integer, we can maintain a count of consecutive same digits and then store the maximum obtained count for each digit into a list. We find the maximum count starting from 9 to 0 since, according to problem, we are required to find the maximum possible good integer which is possible. 

Python Solution:

```python
def maxGoodInteger(num: str) -> str:
    consecutive_counts = [0]*10   # Create a list to store the maximum counts of each digit
    count = 1
    for i in range(1, len(num)):
        if num[i] == num[i-1]:    # If the digits are same then increment the count
            count += 1
        else:                     # Else, store the maximum count for the digit in the consecutive_counts list and reset the count
            consecutive_counts[int(num[i-1])] = max(consecutive_counts[int(num[i-1])], count)
            count = 1

    consecutive_counts[int(num[-1])] = max(consecutive_counts[int(num[-1])], count)    # Update the count for the last digit

    for i in range(9, -1, -1):    # Find the maximum count starting from 9 to 0
        if consecutive_counts[i] >= 3:    # If count is greater than or equal to 3, then return the maximum good integer as string
            return str(i)*3
    return ""    # If no good integer exists, return an empty string
```

This function takes one argument:
- num(string): a string representing a large integer.

This function returns:
- maxGoodInteger(string): a string representing the maximum good integer. If no good integer exists, it returns an empty string.
