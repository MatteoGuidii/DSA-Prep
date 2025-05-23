from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        # Mapping elements in string s
        for ch in s:
            count[ch] += 1

        # Checking if elements of s are present in t
        for ch in t:
            if count[ch] == 0:
                return False
            count[ch] -= 1

        return True
        