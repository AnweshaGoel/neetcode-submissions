from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + (r - l)//2
            total = 0
            for i in piles:
                total += ceil(i/k)
            if total > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res
