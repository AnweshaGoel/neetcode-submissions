class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            res[nums[i]] = i
        print(res)
        for left in range(len(nums)):
            right = target - nums[left]
            if right in res and left != res[right]:
                return [left, res[right]] 