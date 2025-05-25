class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # This is our output array; we initialize to 1s so we can multiply in place
        answer_arr = [1] * n

        # 1) Forward pass: accumulate prefix products
        prefix = 1
        for i in range(n):
            answer_arr[i] = prefix
            prefix *= nums[i]
        # Now answer_arr[i] == product of all nums[0..i-1]

        # 2) Backward pass: accumulate suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            # multiply existing prefix-product by the suffix product
            answer_arr[i] *= suffix
            suffix *= nums[i]
        # Now answer_arr[i] == (product of nums[0..i-1]) * (product of nums[i+1..n-1])

        return answer_arr

# Time Complexity: O(n) — two passes over the list
# Space Complexity: O(1) extra — only a few scalar variables, excluding the output list
