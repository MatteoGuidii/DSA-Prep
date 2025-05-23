from collections import defaultdict 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # complement = target - num; if the complement exists in the map, return its position

        dic = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic:
                return [dic[complement], i]
            
            # Build a map: number → its index
            dic[nums[i]] = i