# 🎨 LeetCode 3208 - Alternating Groups II

**Difficulty:** Medium  
**Problem Link:** [LeetCode 3208](https://leetcode.com/problems/alternating-groups-ii)

---

## 📘 Problem Description

You are given a circular array `colors` and an integer `k`. You must count the number of contiguous **groups of length `k`** (circularly) such that the colors **strictly alternate** (i.e., no two adjacent elements in the group are the same).

---

## 🧪 Examples

### Example 1:
```python
Input: colors = [1,2,1,2,1], k = 3
Output: 3
Explanation: There are 3 alternating groups of length 3.
```

### Example 2:
```python
Input: colors = [1,1,1], k = 2
Output: 0
```

### 🧠 Approach

- Maintain a **sliding window of size** `k`, tracking how many consecutive elements in the window differ from their neighbor.

- A group is valid if it contains exactly `k - 1` alternating transitions.

- To simulate the **circular nature** of the array, use modulo operations where needed.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of the colors array.

- **Space Complexity:** `O(1)`

### 🏷️ Tags

`sliding-window`, `array`, `modulo`, `circular-array`, `medium`