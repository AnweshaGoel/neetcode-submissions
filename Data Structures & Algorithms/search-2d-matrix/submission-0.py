class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        array = 0
        while left <= right:
            array = left + (right - left)//2
            if target < matrix[array][0]:
                right = array - 1
            elif target > matrix[array][-1]:
                left = array + 1
            else:
                break
        left, right = 0, len(matrix[array]) - 1
        while left <= right:
            mid = left + (right - left)//2
            if target < matrix[array][mid]:
                right = mid - 1
            elif target > matrix[array][mid]:
                left = mid + 1
            else:
                return True
        return False
