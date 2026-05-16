# 290. Word Pattern
### Problem Statement
Check if a pattern matches a string s following a bijective mapping.

Each unique character in pattern must map to exactly one unique word in s, and vice versa. The string s is a single space-separated string of words.

## Example
Input: pattern = "abba", s = "dog cat cat dog"
Output: True
Input: pattern = "abba", s = "dog cat cat fish"
Output: False

### Logic: Dual Hash Maps (One-Pass)
To guarantee a strict bijective (two-way) mapping without any crossovers, we track the relationships using two separate dictionaries simultaneously:

pattern_to_word: Ensures a single character from the pattern never links to two different words.
word_to_pattern: Ensures a single word from the string never links to two different pattern characters.
Step-by-Step Execution:
First, split s by spaces into a list of individual words. If the number of characters in pattern does not match the number of words, return False immediately.
Loop through the characters and words side-by-side using zip().
At each step, cross-reference both dictionaries. If a key exists but points to a different value, the pattern is broken, and we return False.
If the pairs pass the check, save the bidirectional link in both maps and continue.

### Complexity
Time Complexity: $O(n)$ — We process the pattern string and the word list exactly once, where $n$ represents the total number of characters in pattern (or words in s).
Space Complexity: $O(w)$ — Where $w$ is the number of unique words/characters stored inside the dual hash maps. In the worst-case scenario, this scales linearly with the size of the input.
