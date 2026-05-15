# 136. Single Number

### Problem Statement
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

---

### Logic 1: Bit Manipulation (XOR)
We use the **XOR** (`^`) logical operator to find the unique number.
- **Property 1**: $X \oplus X = 0$ (Identical numbers cancel out).
- **Property 2**: $X \oplus 0 = X$ (XOR with zero stays the same).
- By XORing all numbers together, all pairs vanish, leaving only the unique value.

### Logic 2: Hash Set
We use a set to track numbers as we iterate.
- If a number is not in the set, we **add** it.
- If it is already in the set, we **remove** it.
- The final remaining element in the set is our answer.

---

### Complexity Comparison

| Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Bit Manipulation** | $O(n)$ | $O(1)$ |
| **Hash Set** | $O(n)$ | $O(n)$ |
