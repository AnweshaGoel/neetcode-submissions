class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        scount = Counter(s)
        tcount = Counter(t)
        if scount == tcount:
            return True
        return False