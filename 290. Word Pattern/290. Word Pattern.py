"""
        Check if a pattern matches a string following a bijective mapping.
        Each character in pattern should map to exactly one word in s, and vice versa.
      
        Args:
            pattern: A string containing the pattern (e.g., "abba")
            s: A space-separated string of words (e.g., "dog cat cat dog")
      
        Returns:
            True if the pattern matches the string, False otherwise
        """
        # Split the string into individual words
        words = s.split()
      
        # If lengths don't match, pattern cannot be followed
        if len(pattern) != len(words):
            return False
      
        # Dictionary to map pattern characters to words
        pattern_to_word = {}
        # Dictionary to map words to pattern characters (ensures bijection)
        word_to_pattern = {}
      
        # Iterate through pattern characters and corresponding words simultaneously
        for pattern_char, word in zip(pattern, words):
            # Check if pattern character already has a different word mapping
            if pattern_char in pattern_to_word and pattern_to_word[pattern_char] != word:
                return False
          
            # Check if word already has a different pattern character mapping
            if word in word_to_pattern and word_to_pattern[word] != pattern_char:
                return False
          
            # Establish the bidirectional mapping
            pattern_to_word[pattern_char] = word
            word_to_pattern[word] = pattern_char
      
        return True
        