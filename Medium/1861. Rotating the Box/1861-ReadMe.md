# 🟦 LeetCode 1861 - Rotating the Box

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1861](https://leetcode.com/problems/rotating-the-box)

---

## 📘 Problem Description

You are given a 2D matrix `box` representing a box filled with stones (`'#'`), obstacles (`'*'`), and empty spaces (`'.'`).

Each stone in the box will fall downwards due to gravity until it hits either the bottom of the box or an obstacle.

After simulating gravity, you are required to rotate the box 90 degrees clockwise and return the final state.

---

## 🧪 Example

### Input:
```python
box = [
    ["#", ".", "#"]
]
```

## Output:
```python
[
    [".", "#", "#"]
]
```

## 🚀 Approach
- Simulate Gravity (Rightward Movement in Each Row):

- - Traverse each row from right to left.

- - Use a pointer to track where the next `#` (stone) should fall.

- - Stones fall to the furthest available empty spot unless blocked by an obstacle (`*`).

- Rotate the Matrix:

- - Use `zip(*box[::-1])` to rotate the 2D matrix 90 degrees clockwise.

## ⏱️ Complexity
- **Time Complexity:** O(m × n)

- **Space Complexity:** O(m × n) (for the rotated output)

## 🏷️ Tags
`matrix`, `simulation`, `rotation`, `gravity`, `leetcode-medium`