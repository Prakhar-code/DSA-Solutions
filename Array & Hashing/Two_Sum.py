# 1. Two Sum
# Problem: https://leetcode.com/problems/two-sum/
# Given an integer array nums of length n and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 6, we return [0, 1].


# Brute Force Approach:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

# Optimal Approach:
# Using Hashing
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i
        return []