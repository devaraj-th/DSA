"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"


"""

def reverse_vowel_string(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = list(s)  # Convert string to a list to allow in-place modification
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l].lower() in vowels and s[r].lower() in vowels:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        elif s[l].lower() not in vowels:
            l += 1  # Move left pointer forward if not a vowel
        elif s[r].lower() not in vowels:
            r -= 1  # Move right pointer backward if not a vowel

    return ''.join(s)  # Convert list back to string

s = "leetcode"
print(reverse_vowel_string(s))  # Output should be "leotcede"