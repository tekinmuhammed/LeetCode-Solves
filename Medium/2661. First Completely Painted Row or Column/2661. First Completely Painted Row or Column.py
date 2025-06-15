class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)
        for idx, num in enumerate(arr):
            r, c = position[num]
            row_count[r] += 1
            col_count[c] += 1
            if row_count[r] == n or col_count[c] ==m:
                return idx
        return -1