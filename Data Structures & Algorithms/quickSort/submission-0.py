# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.help(0, len(pairs)-1, pairs)
    
    def help(self, s, e, pairs):
        if e - s + 1 <= 1:
            return pairs
        
        pivot = pairs[e]
        left = s
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                temp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = temp
                left += 1
        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.help(s, left - 1, pairs)
        self.help(left + 1, e, pairs)
        return pairs



