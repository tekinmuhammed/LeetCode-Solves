# 165. Compare Version Numbers

**Difficulty:** Medium
**Problem Link:** [LeetCode 368](https://leetcode.com/problems/compare-version-numbers/description/)

---

## Problem Description
Given two version numbers, `version1` and `version2`, compare them.  

- Each version number consists of one or more **revision numbers** separated by dots (`"."`).  
- Each revision is an integer without leading zeros.  
- Missing revisions are treated as `0`.  

Return:  
- `-1` if `version1 < version2`  
- `1` if `version1 > version2`  
- `0` if both are equal  

---

### Example 1
**Input:**  
```python
version1 = "1.01", version2 = "1.001"
```

**Output:**  
```python
0
```

**Explanation:** Both are interpreted as `[1, 1]`.  

---

### Example 2
**Input:**  
```python
version1 = "1.0", version2 = "1.0.0"
```

**Output:**  
```python
0
```

**Explanation:** Missing revisions are treated as zero → `[1,0]` vs `[1,0,0]`.  

---

### Example 3
**Input:**  
```python
version1 = "0.1", version2 = "1.1"
```

**Output:**  
```python
-1
```

**Explanation:** First mismatch: `0 < 1`.  

---

## Approach
1. Split both versions by `"."` and convert each part to an integer.  
2. Pad the shorter list with zeros so both have equal length.  
3. Compare element by element:  
   - If `a < b`, return `-1`.  
   - If `a > b`, return `1`.  
4. If no differences are found, return `0`.  

---

## Complexity Analysis
- **Time Complexity:** `O(n)` where `n` is the maximum number of revisions.  
- **Space Complexity:** `O(n)` for storing version lists.  

---

### Tags

`LeetCode-Medium`