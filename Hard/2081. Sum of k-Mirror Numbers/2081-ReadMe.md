# 2081. Sum of k-Mirror Numbers

**Difficulty:** Hard  
**Problem Link:** [LeetCode 2081](https://leetcode.com/problems/sum-of-k-mirror-numbers/)

---

## Problem Description

A **k-mirror number** is a positive integer that is palindromic in both base-10 and base-k. Given integers `k` and `n`, return the sum of the first `n` **k-mirror numbers**.

---

## Example

### Input:
```python
k = 2
n = 5
```

### Output:
`25`

### Explanation:

The first 5 base-2 mirror numbers (palindromic in both base-10 and base-2) are:

- 1 (1 in base-2)

- 3 (11 in base-2)

- 5 (101 in base-2)

- 7 (111 in base-2)

- 9 (1001 in base-2)

Their sum is `1 + 3 + 5 + 7 + 9 = 25`.

### Constraints

- `2 <= k <= 9`

- `1 <= n <= 30`

### Approach

1. **Generate Palindromes in Base-10:**

- We build palindromes by enumerating half of the digits and reflecting them to form full palindromes.

- Two types are considered: even-length and odd-length palindromes.

2. **Check Palindrome in Base-k:**

- For each palindrome generated in base-10, convert it to base-`k` and verify if it's also palindromic.

3. **Accumulate Until n Valid Numbers Found:**

- Continue the process until we find `n` such numbers.

- Maintain a running sum of valid `k`-mirror numbers.

### Time and Space Complexity

- **Time Complexity:**

Roughly `O(n * log(N))`, where `N` is the maximum value of the palindrome tried — due to base conversion and palindrome checks.

- **Space Complexity:**

`O(log(N))` to store digits for the base-`k` palindrome check.

### Tags

`Palindrome`, `Base-Conversion`, `Math`, `Enumeration`

### Notes

- The problem combines palindrome generation with number base manipulation.

- Efficient palindrome enumeration is critical due to the exponential growth of the search space.