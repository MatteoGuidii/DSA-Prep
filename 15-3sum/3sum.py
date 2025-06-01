class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Can we have duplicates?
        # Does the order matter?

        res = []
        nums.sort()

        for i, first in enumerate(nums):
            if first > 0:
                break
            
            # If current num equal previous one, continue (skip this for loop iteration and go to i + 1)
            if i > 0 and first == nums[i - 1]:
                continue

            second, third = i + 1, len(nums) - 1
            while second < third:
                current_sum = first + nums[second] + nums[third]
                if current_sum > 0:
                    third -= 1
                elif current_sum < 0:
                    second += 1
                else:
                    res.append([first, nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1

        return res    
            
# Time Complexity: O(n log n) + O(n^2) = O(n^2)
# Space Complexity: O(1)