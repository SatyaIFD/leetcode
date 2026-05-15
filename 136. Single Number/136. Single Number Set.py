class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Create an empty set to track unique values
        look = set()
        
        # Loop through every element in the array
        for x in nums:
            # Check if the number has already been seen (Average O(1) time)
            if x not in look:
                # First time seeing the number: track it
                look.add(x)
            else:
                # Second time seeing the number: remove it (Average O(1) time)
                look.remove(x)
                
        # The loop eliminates all pairs, leaving exactly one item in the set
        # .pop() extracts and returns that final remaining element
        return look.pop()

# --- COMPLEXITY NOTE ---
# Time Complexity:  O(N) - Iterates through the N elements of the array.
# Space Complexity: O(N) - Allocates extra memory dynamically to store elements.
# Speed:            Slower - Requires object creation and handling potential hash collisions.