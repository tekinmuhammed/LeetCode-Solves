 
# 🧠 Problem Description 
# [Github LeetCode 1331. Rank Transform of an Array ](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Easy/1331.%20Rank%20Transform%20of%20an%20Array)

class Solution:
    q = [*range(1, 10)]

    for x in q:
        d = x % 10
        if d < 9:
            q.append(x * 10 + d + 1)

    def sequentialDigits(self, l: int, h: int) -> list[int]:
        return [x for x in self.q if l <= x <= h]