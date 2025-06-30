# 🔺 LeetCode 3024 - Type of Triangle

**Difficulty:** Easy  
**Problem Link:** [LeetCode 3024](https://leetcode.com/problems/type-of-triangle)

---

## 📘 Problem Description

You are given a list `nums` of 3 positive integers representing the lengths of the sides of a potential triangle.

Return a string representing the **type** of triangle:
- `"equilateral"` if all sides are equal.
- `"isosceles"` if **exactly two** sides are equal.
- `"scalene"` if all three sides are different.
- `"none"` if it is **not** a valid triangle.

> A triangle is **valid** if the sum of any two sides is **greater than** the third.

---

## ✅ Constraints

- `nums.length == 3`
- `1 <= nums[i] <= 100`

---

## 🧠 Approach

1. **Sort the side lengths** to simplify triangle validity check: `a + b > c`.
2. **Check for validity**:
   - If `a + b <= c`, it is **not a triangle**.
3. **Classify the triangle**:
   - If all three sides are equal → `"equilateral"`
   - If exactly two sides are equal → `"isosceles"`
   - If all three sides are different → `"scalene"`

---

### ⏱️ Complexity

- **Time Complexity:** `O(1)`
(Only constant number of operations; list length is fixed at 3)

- **Space Complexity:** `O(1)`

### 📌 Examples
```python
Input: [2, 2, 2]
Output: "equilateral"

Input: [3, 3, 5]
Output: "isosceles"

Input: [3, 4, 5]
Output: "scalene"

Input: [1, 2, 3]
Output: "none"
```

### 🏷️ Tags
`geometry`, `math`, `easy`, `sorting`, `validation`