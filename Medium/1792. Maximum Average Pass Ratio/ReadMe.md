# 🟨 LeetCode 1792 - Maximum Average Pass Ratio

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1792](https://leetcode.com/problems/maximum-average-pass-ratio/)

---

## 📘 Problem Description

You are given a list `classes`, where `classes[i] = [passi, totali]` represents a class with `passi` students who passed out of `totali` total students.

You are also given an integer `extraStudents`. You can assign each of the `extraStudents` to any class, increasing both the number of passing and total students in that class.

Your goal is to **maximize the average pass ratio** across all classes after assigning the extra students.

Return the **maximum possible average pass ratio** after assigning the students optimally.

---

## 🧪 Example

### Input
```python
classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
```

### Output
`1.0`

### Explanation

We can assign one extra student to the second and third classes:

- Class 1: 1/2 → 2/3

- Class 2: 3/5 → 4/6

- Class 3: 2/2 → 3/3

The average pass ratio becomes:
`(2/3 + 4/6 + 3/3) / 3 = 1.0`

### 🚀 Approach

We use a **max heap** to always assign the next extra student to the class that yields the maximum improvement in average pass ratio.

**Steps:**
1. Define an `improvement` function that calculates the gain in pass ratio when adding a student to a class.

2. Use a **max heap** (negating the improvement value for Python's min-heap) to store all classes sorted by their potential improvement.

3. For each extra student:

- Pop the class with the highest improvement.

- Add the student (increment pass and total).

- Push the updated class back into the heap.

4. After all students are assigned, compute the final average.

### ⏱️ Complexity

- **Time Complexity:** `O((n + extraStudents) * log n)`

- - n = number of classes. Each heap operation is log n and we do it for each extra student.

- **Space Complexity:** `O(n)`

- - For the heap.

### 🏷️ Tags

`heap`, `priority-queue`, `greedy`, `math`, `leetcode-medium`