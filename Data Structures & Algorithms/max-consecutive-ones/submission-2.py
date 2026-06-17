class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        best = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            else:
                curr = 0
            if curr > best:
                best = curr
        return best
