class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0

        if n < 3:
            return 0
        
        left, right = 0, n - 1
        left_max, right_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        
        return ans

# Time Complexity: O(n)
# Space Complexity: O(1)