# 36. Valid Sudoku

# **Difficulty:** Medium  
# **Link:** [LeetCode 36](https://leetcode.com/problems/valid-sudoku/)

# 🧠 Problem Description 
# [Github LeetCode 36. Valid Sudoku](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/36.%20Valid%20Sudoku)

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                # satır kontrol
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # sütun kontrol
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # 3x3 kutu kontrol
                box_index = (r // 3) * 3 + (c // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True