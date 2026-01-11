class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # Histogram yüksekliklerini güncelle
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # Histogramda en büyük dikdörtgen
            stack = []
            for i in range(cols + 1):
                cur_height = heights[i] if i < cols else 0
                while stack and cur_height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * width)
                stack.append(i)
        
        return max_area