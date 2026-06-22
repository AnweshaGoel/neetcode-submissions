class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = nums1[:m]
        i = j = k = 0
        while i < len(arr) and j < len(nums2):
            if arr[i] <= nums2[j]:
                nums1[k] = arr[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i < len(arr):
            nums1[k] = arr[i]
            i += 1
            k += 1
        while j < len(nums2):
            nums1[k] = nums2[j]
            j += 1
            k += 1
