from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = defaultdict(int)
        
        for n in nums:
            dic[n] += 1
        
        # It's a list
        new_dic = sorted(
            dic.keys(),              # The items to sort
            key = lambda x: dic[x],  # Use their counts as the sort-value
            reverse = True           # From high to low
            )

        # [start:stop:step] --> [:k] means up to k
        return new_dic[:k]