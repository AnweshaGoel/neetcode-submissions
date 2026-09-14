class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                return True
        return False