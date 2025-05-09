"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""

def reverse_string(arr):
# Using two-pointer technique
    l = 0
    r = len(arr) - 1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1  
        r -= 1  

    return arr

s = ["H", "a", "n", "n", "a", "h"]

print(reverse_string(s))  