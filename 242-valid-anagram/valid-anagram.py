class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        hashS = {}
        hashT = {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        
        return hashS == hashT


# Time: O(n)
# Space: O(1)