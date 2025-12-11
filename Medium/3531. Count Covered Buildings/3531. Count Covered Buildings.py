class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        # row = x, col = y
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)
        
        # satır ve sütunlardaki değerleri sırala
        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()
        
        def has_left(row_list, y):
            # row_list sorted
            # solda bina -> y2 < y
            return row_list[0] < y
        
        def has_right(row_list, y):
            # sağda bina -> y2 > y
            return row_list[-1] > y
        
        def has_up(col_list, x):
            # yukarıda bina -> x2 < x
            return col_list[0] < x
        
        def has_down(col_list, x):
            # aşağıda bina -> x2 > x
            return col_list[-1] > x
        
        covered = 0
        
        for x, y in buildings:
            row_list = rows[x]
            col_list = cols[y]
            
            if (has_left(row_list, y) and
                has_right(row_list, y) and
                has_up(col_list, x) and
                has_down(col_list, x)):
                covered += 1
        
        return covered