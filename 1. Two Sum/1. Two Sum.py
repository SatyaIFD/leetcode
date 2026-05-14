class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number as key and its index as value
        d = {}

        # Loop through the list with both index (i) and value (n)
        for i, n in enumerate(nums):
            # Calculate the number needed to reach the target
            complement = target - n
            
            # Check if the complement exists in the dictionary
            if complement in d:
                # If found, return the indices of the complement and current number
                return [d[complement], i]
            
            # Otherwise, store the current number and its index in the dictionary
            d[n] = i
                    