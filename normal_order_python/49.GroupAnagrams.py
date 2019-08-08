'''

49. Group Anagrams

Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

'''
strs = ["tot","ton","not","rex","pig","ago","maj","the","six","gap","rye","arc","eve","hot","wot","fox","ave","jug","mai","uzi","fin","god"]
class Solution:
    def groupAnagrams(self, strs: list) -> list:
        res = {}
        for i in strs:
            l = tuple(sorted(i))
            # l = ''.join(sorted(i))            
            # pay attemtion to 'sorted(i)'

            if l in res:
                res[l].append(i)
            else:
                res[l] = [i]
        return list(res.values())

s = Solution()
print(s.groupAnagrams(strs))                