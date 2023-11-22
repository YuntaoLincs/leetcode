"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters
"""
# new info:
#   sorted() can be used to sort the string value, and print(sorted(s)) = [,]
#   list(m.values()), can directly trans m.values() into a list
#   join can concat the list value into a string
class Solution(object):
    def __init__(self):
        pass
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for i in strs:

            #temp = []
            #for t in i:
                #temp.append(t)
            #temp.sort()
            s = "".join(sorted(i))
            #print(sorted(i))
            if s in m:
                m[s].append(i)
            else:
                m[s] = [i]
        return list(m.values())


    
strs = ["eat","tea","tan","ate","nat","bat"]
concat
a = Solution()
r = a.groupAnagrams(strs)

print(r)
