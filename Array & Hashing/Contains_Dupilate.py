# 217. Contains Duplicate
# Problem: https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false


# Brute Force Approach:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False


# Optimal Approach:
# Using Hashing
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hash_set = set()
 
        for i in range(n):
            if nums[i] in hash_set:
                return True
            else:
                hash_set.add(nums[i])
        return False