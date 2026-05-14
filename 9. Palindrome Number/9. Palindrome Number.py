class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Handle edge cases
        # Negative numbers are not palindromes (e.g., -121 != 121-)
        # Numbers ending in 0 are not palindromes, unless the number is actually 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        
        # Step 2: Reverse only the right half of the number
        # We know we've reached the middle when 'x' is no longer
        # greater than our 'reversed_half'
        while x > reversed_half:
            # Pop the last digit from x and push it onto reversed_half
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Step 3: Check for equality
        # For even lengths (e.g., 1221), x will be 12 and reversed_half will be 12.
        # For odd lengths (e.g., 121), x will be 1 and reversed_half will be 12.
        # We use // 10 to ignore the middle digit in odd-length numbers.
        return x == reversed_half or x == reversed_half // 10
        