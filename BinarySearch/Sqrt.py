class Solution:
    
    """
    Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

    You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
    """
    
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x 
        mid = 0
        while l <= r :
            mid = l + (r - l)//2
            sq = mid * mid
            if sq > x:
                r = mid - 1
            elif sq < x : 
                l = mid + 1
            else:
                return mid
        return r
    

# Create an instance of Solution
solution = Solution()

# Test cases
print(solution.mySqrt(4))  # Expected output: 2, because 2 * 2 = 4
print(solution.mySqrt(9))  # Expected output: 2, because 2 * 2 = 4 < 8 and 3 * 3 = 9 > 8
print(solution.mySqrt(16)) # Expected output: 4, because 4 * 4 = 16
print(solution.mySqrt(1))  # Expected output: 1, because 1 * 1 = 1
print(solution.mySqrt(0))  # Expected output: 0, because 0 * 0 = 0
