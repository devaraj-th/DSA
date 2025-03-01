""""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".


"""

def word_pattern(pattern, string):

    words= string.split()

    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern,words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
            
        if word in word_to_char:
            if word_to_char[word] !=char:
                return False
            
        char_to_word[char]=word
        word_to_char[word]=char

    return True

pattern = "abba"
s = "dog cat cat fish"
print(word_pattern(pattern,s))
