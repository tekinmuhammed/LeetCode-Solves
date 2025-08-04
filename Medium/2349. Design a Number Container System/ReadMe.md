# 📦 LeetCode 2349 - Design a Number Container System

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2349](https://leetcode.com/problems/design-a-number-container-system/)

---

## 📘 Problem Description

Design a system that supports the following operations:

- `change(index, number)`: Stores the number at the given index.
- `find(number)`: Returns the **smallest index** for which the stored number equals `number`. If no such index exists, return `-1`.

Multiple updates may happen at the same index.

---

## 🧪 Example

```python
obj = NumberContainers()
obj.change(2, 10)
obj.change(1, 10)
obj.change(2, 5)
obj.find(10)  # Returns 1
obj.find(5)   # Returns 2
obj.find(20)  # Returns -1
```

### Explanation:

- Index 2 was updated from 10 to 5. So `find(10)` returns 1.

- `find(5)` returns 2 because index 2 now contains 5.

- `find(20)` returns -1 since 20 was never inserted.

### 🧠 Approach & Intuition

- Use a dictionary `index_to_number` to map each index to its current number.

- Use a min-heap for each number to quickly get the smallest index where it exists.

- During `find`, some indices in the heap might be outdated, so we clean them up on the fly.

### ⏱️ Complexity

- **Time Complexity**:

- - `change()`: `O(log n)` (due to heap push)

- - `find()`: Amortized `O(log n)` (due to cleanup of outdated indices)

- **Space Complexity:** `O(n)` — storing mappings and heaps.

### 🏷️ Tags

`design`, `hashmap`, `heap`, `priority-queue`, `leetcode-medium`