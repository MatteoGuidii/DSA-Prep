class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1

# Time Complexity: O(1)
# We use a two-pointer approach on the sorted list.
# In the worst case, each pointer moves at most n steps total, performing constant work per iteration.
        
# Space Complexity: O(1)
# Only a fixed number of extra variables are used (left, right, total), regardless of input size.