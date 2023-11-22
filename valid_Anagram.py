"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    m = {}
    for i in s:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1
    for i in t:
        if i in m:
            if m[i] != 0:
                m[i] -= 1
        else:
            return False
    for i in m:
        if m[i] != 0:
            return False
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))
    
