# 🎲 LeetCode 909 - Snakes and Ladders

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 909](https://leetcode.com/problems/snakes-and-ladders)

# 🧠 Problem Description 
# [Github LeetCode 909 - Snakes and Ladders](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/909.%20Snakes%20and%20Ladders)

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        length = len(board)
        board.reverse()
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return[r, c]

        q = deque()
        q.append([1, 0])
        visit = set()
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1