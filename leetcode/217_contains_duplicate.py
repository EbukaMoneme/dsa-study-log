## Question:

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Example 1:

# Input: nums = [1,2,3,1]
# Output: true

## Answer:

# Time complexity: O(n) —> might have to go through the whole array
# Space complexity: O(n) —> possible to add every value of the array to the hashmap
# Data Structure: Array
# Solution Pattern: Hashmap/Hashset
# Method
    # Go through each value in the array
    # If the value is in your hashset/hashmap, return True
    # otherwise return False

# Solution using hashmap and enumerate:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = {}
        for index, value in enumerate(nums):
            if value in record:
                return True
            record[value] = index
        return False
    
# Solution using hashset:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for value in nums:
            if value in hashSet: 
                return True
            hashSet.add(value)
        return False