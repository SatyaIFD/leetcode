# 9. Palindrome Number

### Problem Statement
Given an integer x, return true if x is a palindrome, and false otherwise.

### Logic: Reversing the Half
Instead of reversing the whole number (which might cause overflow in some languages) or converting to a string, we reverse only the right half of the number.
- We stop when the reversed part becomes greater than or equal to the remaining left part.
- For odd-length numbers, we divide the reversed part by 10 to remove the middle digit.

### Complexity
- **Time Complexity**: O(log₁₀(n))
- **Space Complexity**: O(1)
