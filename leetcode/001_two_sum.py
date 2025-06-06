## Question:

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

## Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

## Answer:

# Time Complexity: O(n) -> because you map through the entire array nums
# Space Complexity: O(n) —> because you could add every value of the array into the hashmap
# Data Structure: Array
# Solution Pattern: Hashmap/Dictionary
# Method
    # For each value check if `target - value` is present in the hash map
    # Yes? return the current index + values’ index
    # No? add the value (key) and index (value) to the hash map
# Solution using enumerate:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for index, value in enumerate(nums):
            diff = target - nums[index]
            if diff in record:
                return [index, record[diff]]
            record[value] = index