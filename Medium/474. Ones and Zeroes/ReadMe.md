# 🔢 474. Ones and Zeroes

**Difficulty:** Medium  
**Problem Link:** [LeetCode 474](https://leetcode.com/problems/ones-and-zeroes/description/)

## 🧩 Problem Description
You are given an array of binary strings `strs` and two integers `m` and `n`.

Return the **size of the largest subset** of `strs` such that the subset contains **at most `m` zeros and `n` ones** in total.

Each string can be used **at most once** — this makes it a **0/1 knapsack problem**, where:
- Each string has a “cost” (its number of 0s and 1s),
- and a “value” of 1 (since we’re counting how many strings can fit).

---

## 💡 Example

### Example 1
**Input:**
```python
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
```

**Output:**
```python
4
```

**Explanation:**
We can form a subset of up to **5 zeros** and **3 ones** like:
```python
["10", "0001", "1", "0"]
```
- ✅ Total zeros = 5  
- ✅ Total ones = 3  
- ✅ 4 strings in total — the maximum possible.

---

## 🧠 Intuition

This problem can be seen as a **2D knapsack problem**, where:
- The “capacity” is defined by two constraints: number of `0`s (`m`) and number of `1`s (`n`).
- Each binary string is an “item” that consumes some of each resource.

We want to **maximize the number of strings** we can include **without exceeding** the available zeros and ones.

### 🔍 Analogy
Think of having:
- `m` empty slots for zeros,  
- `n` empty slots for ones.

Each string uses up some of these slots.
We fill them optimally to maximize how many strings fit — this is exactly what dynamic programming (DP) solves.

---

## 🧩 Implementation

```python
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # DP table where dp[i][j] = max subset size using at most i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            # Traverse backwards to avoid overwriting previous states
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])

        return dp[m][n]
```
---

## 🧮 Step-by-Step Example

### Example
**Input:**
```python
strs = ["10", "0", "1"]
m = 1, n = 1
```

### Process:
| Step | String | zeros | ones | DP Effect |
|------|---------|--------|------|------------|
| 1 | "10" | 1 | 1 | Can fit if we have 1 zero & 1 one |
| 2 | "0" | 1 | 0 | Uses only one zero |
| 3 | "1" | 0 | 1 | Uses only one one |

At the end:
- You can include either `["0", "1"]` or just `"10"`.  
✅ Both options give **2** strings, which is the optimal result.

---

## ⏱️ Complexity Analysis

| Type | Complexity |
|------|-------------|
| **Time Complexity** | `O(len(strs) * m * n)` |
| **Space Complexity** | `O(m * n)` |

---

## 🧭 Summary

| Concept | Description |
|----------|--------------|
| **Problem Type** | 0/1 Knapsack (2D constraints) |
| **State Definition** | `dp[i][j] = max subset size using ≤ i zeros and ≤ j ones` |
| **Transition** | `dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])` |
| **Time Complexity** | `O(len(strs) * m * n)` |
| **Space Complexity** | `O(m * n)` |

---

### 🧠 Key Insight
Each binary string is like an "item" with **two resource costs** (zeros and ones).  
We use a **2D DP knapsack** to decide optimally which strings to include.

> 🏆 *This problem is a classic multidimensional DP example — simple idea, powerful technique.*