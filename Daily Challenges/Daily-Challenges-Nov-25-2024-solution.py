# 🧩 LeetCode 773 - Sliding Puzzle

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 773](https://leetcode.com/problems/sliding-puzzle/)

# 🧠 Problem Description
# [Github LeetCode 773 - Sliding Puzzle](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/773.%20Sliding%20Puzzle)

from collections import deque

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        target = "123450"
        start = "".join(str(num) for row in board for num in row)

        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        queue = deque([(start, 0)])
        visited = set([start])

        while queue:
            current, steps = queue.popleft()
            if current == target:
                return steps
            zero_index = current.index('0')
            for neighbor in neighbors[zero_index]:
                new_board = list(current)
                new_board[zero_index], new_board[neighbor] = new_board[neighbor], new_board[zero_index]
                new_state = "".join(new_board)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
        return -1