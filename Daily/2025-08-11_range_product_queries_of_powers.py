"""
Title     : Range Product Queries of Powers
Difficulty: Medium

Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.
You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.
Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.
 
Example 1:

Input: n = 15, queries = [[0,1],[2,2],[0,3]]
Output: [2,4,64]
Explanation:
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 109 + 7 yields the same answer, so [2,4,64] is returned.

Example 2:

Input: n = 2, queries = [[0,0]]
Output: [2]
Explanation:
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 109 + 7 is the same, so [2] is returned.

 
Constraints:

1 <= n <= 109
1 <= queries.length <= 105
0 <= starti <= endi < powers.length
"""

# Your solution below:
Let's write Python solution in the form of a function. 

First, we need to build list of powers. Given number 'n', we can build the minimum-sized list of powers of 2 as follows:

- If n is a power of 2, then our list will contain only that number.
- If n is not a power of 2, then our list will contain n // 2 raised to the power of 2, and the next number will be n minus the previous number.

It's important to note that the modulo operation obeys the distributive law, meaning that we can take the product of the elements modulo 10^9 + 7 directly instead of first calculating the product and then taking the modulo. This allows us to avoid overflow issues.


    def rangeProductQueries(n, queries):
        # Modulus for avoiding overflow
        MOD = 10**9 + 7

        # Generate the list of powers
        powers = []
        while n:
            # Find the largest power of 2 that is less than or equal to n
            power = 1
            while (power << 1) <= n:
                power <<= 1
            powers.append(power)
            n -= power

        # Precompute prefix products
        prefix = [1]
        for x in powers:
            prefix.append(prefix[-1] * x % MOD)

        # Answer queries
        return [(prefix[right + 1] * pow(prefix[left], MOD - 2, MOD)) % MOD for left, right in queries]


The function rangeProductQueries first generates the list of powers as describe above. Then it precomputes prefix products, where prefix[i] is the product of first 'i' elements in powers. 

In the last step, it answers each query by multiplying prefix[right + 1] with the modular inverse of prefix[left].

It uses the formula (prefix[right + 1] / prefix[left]) % MOD, where pow(prefix[left], MOD - 2, MOD) calculates modular inverse of prefix[left] using Fermat's Little Theorem.
