class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Initialize variables
        n = len(nums)
        answer_arr = [1] * n

        # Calculate Prefix Product
        prefix = 1
        for i in range(n):
            answer_arr[i] = prefix
            prefix *= nums[i]
        # After this, answer_arr[i] = product of all elements before index i.


        # Calculate Suffix Product
        suffix = 1
        for i in range(n - 1, -1, -1):
            # equivalent to: answer_arr[i] = (prefix product up to i−1) * (suffix product from i+1 to end)
            answer_arr[i] *= suffix
            suffix *= nums[i]

        return answer_arr
        