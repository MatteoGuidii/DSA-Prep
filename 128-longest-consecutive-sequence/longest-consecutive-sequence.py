class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Nums as set 
        nums_set = set(nums)
        longest = 0

        # Iterate over nums
        for num in nums_set:
        # Check if num - 1 not in set(nums)
        # Initialize variable to count the sequence of consequent number (n, n + 1, n + 2.... n + n)
            if (num - 1) not in nums_set:
                length = 0
                while (num + length) in nums_set: # While sequence's numbers present, keep counting
                    length += 1
                
                longest = max(longest, length)

        return longest