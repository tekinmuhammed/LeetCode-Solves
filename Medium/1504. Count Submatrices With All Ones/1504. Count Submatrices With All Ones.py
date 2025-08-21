class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        
        # Height matrix (her hücre için üst üste gelen 1'ler)
        height = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    height[i][j] = 1 if i == 0 else height[i-1][j] + 1
        
        total = 0
        # Her satır için dikdörtgenleri say
        for i in range(rows):
            for j in range(cols):
                if height[i][j] > 0:
                    min_height = height[i][j]
                    # sola doğru genişlet
                    for k in range(j, -1, -1):
                        if height[i][k] == 0:
                            break
                        min_height = min(min_height, height[i][k])
                        total += min_height
        return total