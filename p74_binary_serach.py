from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0])-1
        while l<=r:
            m = int(l + (r-l)/2)
            m_r = m // len(matrix[0])
            m_c = m % len(matrix[0])
            if matrix[m_r][m_c] == target:
                return True
            elif matrix[m_r][m_c] > target:
                r = m-1
            else:
                l = m+1
            print(m)
        return False