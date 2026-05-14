# 1. Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Logic: Hash Map (One-Pass)
1. We use a dictionary (hash map) to keep track of numbers we have already seen.
2. For every number, we check if its "partner" (target - current) is already in the dictionary.
3. This allows us to find the answer in a single scan of the array.

## Complexity
- **Time Complexity:** (n)$ — We only loop through the list once.
- **Space Complexity:** (n)$ — In the worst case, we store every number in the dictionary.
