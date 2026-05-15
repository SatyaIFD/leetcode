class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize result tracker to 0
        # XORing any number with 0 leaves the number unchanged (0 ^ X = X)
        result = 0
        
        # Iterate through every integer in the array
        for x in nums:
            # Apply the Bitwise XOR operator (^)
            # Property 1: X ^ X = 0 (Identical numbers cancel each other out)
            # Property 2: Order does not matter (A ^ B ^ A is the same as A ^ A ^ B)
            result ^= x
            
        # Every duplicate pair cancels out to 0, leaving only the unique number
        return result

# --- COMPLEXITY NOTE ---
# Time Complexity:  O(N) - Scans the input array exactly once.
# Space Complexity: O(1) - Uses only one integer variable (constant extra space).
# Speed:            Faster - Executes directly on hardware CPU registers.