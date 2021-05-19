from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            if d.get(key):
                d[key].append(s)
            else:
                d[key] = [s]
        result = []
        for key in d.keys():
            result.append(d[key])
        return result

sl = Solution()
print(sl.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))