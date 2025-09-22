# 3005. Count Elements With Maximum Frequency

**Difficulty:** Easy  
**Link:** [LeetCode 3005](https://leetcode.com/problems/count-elements-with-maximum-frequency/description/)  

---

## Problem Description
You are given an integer array `nums`.  
- First, find the **frequency** of each element.  
- Then, identify the **maximum frequency** among them.  
- Finally, return the **total count of elements** whose frequency is equal to this maximum frequency.  

🔹 In other words, instead of returning the number of distinct elements with the maximum frequency, we return how many elements in total appear with that maximum frequency.

### Example 1
**Input:**
```python
nums = [1,2,2,3,1,4]
```

**Step 1:** Frequencies → `{1: 2, 2: 2, 3: 1, 4: 1}`  
**Step 2:** Maximum frequency = `2`  
**Step 3:** Elements with frequency 2 → `1, 2` (each appears twice)  

**Output:**
```python
4
```

---

### Example 2
**Input:**
```python
nums = [1,2,3,4,5]
```

**Step 1:** Frequencies → `{1:1, 2:1, 3:1, 4:1, 5:1}`  
**Step 2:** Maximum frequency = `1`  
**Step 3:** All numbers appear once → total = `5`  

**Output:**

```python
5
```

---

## Approach
1. Use `collections.Counter` to calculate the frequency of each element.  
2. Find the **maximum frequency** using `max(freq.values())`.  
3. Iterate through the frequency dictionary and sum up all values that equal this maximum frequency.  

---

## Complexity Analysis
- **Time Complexity:**  
  - `O(n)` to build the frequency dictionary.  
  - `O(k)` to compute the sum where `k` is the number of distinct elements.  
  - Overall → **O(n)**.  

- **Space Complexity:**  
  - `O(k)` for storing frequencies of distinct elements.  

### Tags
`LeetCode-Easy`, `Array`