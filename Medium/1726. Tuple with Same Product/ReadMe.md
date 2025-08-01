# 🧮 LeetCode 1726 - Tuple with Same Product

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1726](https://leetcode.com/problems/tuple-with-same-product/)

---

## 🧩 Problem Description

Given an array `nums` of **distinct** positive integers, return the number of tuples `(a, b, c, d)` such that:

- `nums[a] * nums[b] == nums[c] * nums[d]`
- `a`, `b`, `c`, and `d` are all distinct.

The order of the tuple matters — different permutations count as separate tuples.

---

## 🔍 Example

### Input:
```python
nums = [2, 3, 4, 6]
```

### Output:
```python
8
```

### Explanation:

Valid tuples with equal products:

- (2,6,3,4), (2,6,4,3), (6,2,3,4), (6,2,4,3)

- (3,4,2,6), (3,4,6,2), (4,3,2,6), (4,3,6,2)

Each unique product match can form 8 permutations.

### 🧠 Approach & Intuition

1. Iterate over all pairs `(i, j)` in the array.

2. Calculate the product of `nums[i] * nums[j]`.

3. Use a hashmap (`product_map`) to track how many times each product has occurred.

4. If a product has occurred `k` times before, then each new pair can form `8 * k` new valid tuples — because:

- Each of the `k` previous pairs can be paired with the new one in `4 * 2 = 8` permutations.

### ⏱️ Complexity

- **Time Complexity:** `O(n²)`
Checking all unique pairs of elements.

- **Space Complexity:** `O(n²)`
In worst case, all products may be unique.

### 🏷️ Tags

`array`, `hash-map`, `combinatorics`, `math`, `brute-force`