# 1320. Minimum Distance to Type a Word Using Two Fingers

**Difficulty:** Hard
**Problem Link:** [LeetCode 1320](https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/description/)

---

## Problem Description

You have a keyboard layout where 26 uppercase English letters are arranged in a **6-column grid** (A-F in the first row, G-L in the second, and so on). 

The distance between two letters is the **Manhattan distance**: 
$$dist(p, q) = |x_1 - x_2| + |y_1 - y_2|$$

You have two fingers. Initially, they can be placed on any two letters for free (distance 0). Given a string `word`, return the **minimum total distance** to type the entire word using two fingers.

---

## Approach: 3D Dynamic Programming

The problem requires tracking the positions of both fingers to calculate the cost of moving either one to the next character.

### Key Ideas:
1.  **State Definition:** `dp[i][f1][f2]` represents the minimum distance to type the first `i` characters, with Finger 1 at position `f1` and Finger 2 at `f2`.
2.  **Manhattan Distance on Grid:** Each character index $c \in [0, 25]$ maps to a 2D coordinate:
    - $x = c // 6$
    - $y = c \% 6$
3.  **Transitions:** For each new character `cur` in the word:
    - We can move the finger that typed the previous character (`prev`) to `cur`.
    - We can move the "idle" finger (from any possible position `k`) to `cur`.
4.  **Base Case:** The first character can be reached by either finger with 0 cost.


---

## Code

```python
class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        BIG = 2**30
        # dp[i][f1][f2]: min distance to type word[:i+1] 
        # with fingers at f1 and f2 positions
        dp = [[[BIG] * 26 for _ in range(26)] for _ in range(n)]
        
        # Initial step: First character is typed for free
        first_char = ord(word[0]) - 65
        for i in range(26):
            dp[0][i][first_char] = 0
            dp[0][first_char][i] = 0

        def getDistance(p, q):
            # Calculate Manhattan distance on the 6-column grid
            x1, y1 = p // 6, p % 6
            x2, y2 = q // 6, q % 6
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(1, n):
            cur = ord(word[i]) - 65
            prev = ord(word[i - 1]) - 65
            d = getDistance(prev, cur)
            
            for j in range(26):
                # Case 1: Move the same finger that typed 'prev' to 'cur'
                dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][prev][j] + d)
                dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][prev] + d)
                
                # Case 2: Move the other finger (previously at 'k') to 'cur'
                if prev == j:
                    for k in range(26):
                        d0 = getDistance(k, cur)
                        dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][k][j] + d0)
                        dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][k] + d0)

        # Final answer is the minimum in the last DP state across all finger positions
        ans = min(min(dp[n - 1][x]) for x in range(26))
        return ans