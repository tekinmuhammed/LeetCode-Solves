# 🚫 LeetCode 2364 - Count Number of Bad Pairs

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2364](https://leetcode.com/problems/count-number-of-bad-pairs/)

---

## 📘 Problem Description

You are given a **0-indexed** integer array `nums`.

A pair `(i, j)` is called a **bad pair** if:

- `i < j` and  
- `j - i != nums[j] - nums[i]`

Return the **total number of bad pairs** in the array.

---

## 🧪 Example

### Input:
```python
nums = [4, 1, 3, 3]
```

### Output:
```python
5
```

### Explanation:

There are 6 possible pairs:

- (0,1): 1-0 != 1-4 → bad ✅

- (0,2): 2-0 != 3-4 → bad ✅

- (0,3): 3-0 != 3-4 → bad ✅

- (1,2): 2-1 != 3-1 → bad ✅

- (1,3): 3-1 != 3-1 → bad ✅

- (2,3): 3-2 == 3-3 → good ❌

Total bad pairs = 5

### 🚀 Approach

Instead of checking each pair individually (which takes O(n²)), we notice:

- For a pair `(i, j)` to be good, `j - i == nums[j] - nums[i]`, or equivalently:
`j - nums[j] == i - nums[i]`

So we define `diff = i - nums[i]` for each element.

- If multiple indices share the same `diff`, we can count how many good pairs exist with that `diff`.

- Total number of possible pairs: `n * (n - 1) / 2`

- Bad pairs = Total pairs - Good pairs

### ⏱️ Complexity

- **Time Complexity:** `O(n)`

- **Space Complexity:** `O(n)` — for storing differences in a hash map

### 🏷️ Tags

`hashmap`, `math`, `counting`, `prefix`, `leetcode-medium`