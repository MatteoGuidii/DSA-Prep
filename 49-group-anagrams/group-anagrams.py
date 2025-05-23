from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        # Sort the current word, store it in the dict
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            dic[sorted_word].append(strs[i])

        # Return list of results. In dic they are store as list, so add an outer list
        return list(dic.values())