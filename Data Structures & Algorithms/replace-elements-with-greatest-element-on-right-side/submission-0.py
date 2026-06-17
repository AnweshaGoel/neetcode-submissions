class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rep = arr[0]
        for i in range(len(arr) - 1):
            if arr[i] == rep:
                rep = max(arr[i+1:])
            arr[i] = rep
        arr[-1] = -1
        return arr
        