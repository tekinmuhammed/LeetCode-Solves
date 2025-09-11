# 2785. Sort Vowels in a String

**Difficulty:** Medium  
**Link:** [LeetCode 2785](https://leetcode.com/problems/sort-vowels-in-a-string/)

---

## Problem Description
Given a string `s`, sort the **vowels** in `s` in ascending order according to their ASCII values, while keeping all consonants and other characters in their original positions.

Vowels are defined as:  
'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'

---

## Example 1
**Input:**
```python
s = "lEetcOde"
```

**Output:**
```python
"lEOtcdee"
```

**Explanation:**
- Vowels in `s`: `E, e, O, e`
- Sorted vowels: `E, O, e, e`
- Replace vowels in order while keeping consonants fixed → `"lEOtcdee"`

---

## Example 2
**Input:**
```python
s = "lYmpH"
```

**Output:**
```python
"lYmpH"
```

**Explanation:**
- No vowels present → string remains unchanged.

---

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of letters and possibly other printable ASCII characters.

---

## Approach

### Key Idea
- Extract all vowels into a list.
- Sort this list by ASCII order.
- Traverse original string:
  - If current char is a vowel → replace with the next sorted vowel.
  - Else → keep as is.

### Algorithm
1. Identify vowels using a set for O(1) lookup.
2. Collect all vowels from `s` into `vowel_list`.
3. Sort `vowel_list`.
4. Iterate through `s`, building result:
   - If char is vowel → append `vowel_list[idx]` and increment `idx`.
   - Otherwise, append char directly.
5. Return joined string.

---

## Time and Space Complexity
- **Time Complexity:**  
  - Collect vowels: O(n)  
  - Sort vowels: O(k log k), where k = number of vowels  
  - Rebuild string: O(n)  
  - Total: **O(n + k log k)**  

- **Space Complexity:** O(k) for vowel storage + O(n) for result.

---

## Tags
String, Sorting, Two-Pointer, Greedy

---

## Notes
- Sorting is based on ASCII values, so `A < E < O < U < a < e < i < o < u`.
- If no vowels exist, the string remains unchanged.