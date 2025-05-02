# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# A palindrome is a string that reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Note that the given s is not empty.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:   
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.


# Brute Force Approach:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

# Optimal Approach:
# Using Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True