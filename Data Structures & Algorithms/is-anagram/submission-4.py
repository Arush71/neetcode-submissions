class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hs = {}
        ht = {}
        for c in s:
            hs[c] = hs.get(c, 0) + 1
        for c in t:
            ht[c] = ht.get(c, 0) + 1
        return hs == ht


        