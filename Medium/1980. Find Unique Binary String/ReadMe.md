# 1980. Find Unique Binary String

**Difficulty:** Medium  
**Problem Link:** [LeetCode 1980](https://leetcode.com/problems/find-unique-binary-string/description/)

---

## Problem Description

Given an array of strings `nums` containing $n$ **unique** binary strings each of length $n$, return a binary string of length $n$ that **does not appear** in `nums`. If there are multiple answers, you may return any of them.

---

## Approach: Cantor's Diagonal Argument

This problem can be solved brilliantly using **Cantor's Diagonal Argument**. Instead of generating all $2^n$ possible strings or using a Hash Set to track seen strings, we construct a unique string by ensuring it differs from every string in the input at at least one position.

### Key Ideas:
1.  **The Diagonal Strategy:** We build a result string of length $n$. For each index $i$ from $0$ to $n-1$, we look at the $i^{th}$ character of the $i^{th}$ string in the input (`nums[i][i]`).
2.  **Flipping the Bit:** - If `nums[i][i]` is `'0'`, we set our result's $i^{th}$ bit to `'1'`.
    - If `nums[i][i]` is `'1'`, we set our result's $i^{th}$ bit to `'0'`.
3.  **Guaranteed Uniqueness:** By doing this, our constructed string is guaranteed to be different from the first string at index 0, different from the second string at index 1, and so on. Since it differs from every string in `nums` at at least one position, it cannot be in the list.

---

## Code

```python
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        res = []
        
        # Iterate through each string in nums using its index
        for i in range(len(nums)):
            # Look at the i-th character of the i-th string
            # and pick the opposite bit
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
        
        # Join the characters to form the final unique string
        return "".join(res)
```

---

## Example Walkthrough

**Input:** `nums = ["01", "10"]` ($n=2$)

1.  **Index $i=0$:** Look at `nums[0][0]` which is `'0'`. Our `res[0]` becomes `'1'`.
2.  **Index $i=1$:** Look at `nums[1][1]` which is `'0'`. Our `res[1]` becomes `'1'`.

**Result:** `"11"`  
*(Check: "11" is not in ["01", "10"]. Correct!)*

**Input:** `nums = ["000", "111", "011"]` ($n=3$)

1.  **$i=0$:** `nums[0][0]` is `'0'` $\rightarrow$ `res[0]` = `'1'`
2.  **$i=1$:** `nums[1][1]` is `'1'` $\rightarrow$ `res[1]` = `'0'`
3.  **$i=2$:** `nums[2][2]` is `'1'` $\rightarrow$ `res[2]` = `'0'`

**Result:** `"100"`  
*(Check: "100" is not in the input. Correct!)*

---

## Complexity Analysis

* **Time Complexity:** $O(n)$
    - We only iterate through the list of $n$ strings once, accessing one character from each.
* **Space Complexity:** $O(n)$ (or $O(1)$ excluding output)
    - We store $n$ characters in a list to join them at the end. No extra sets or large data structures are needed.

---

## Tags
`Array`, `String`, `Backtracking`, `Cantor's-Diagonalization`, `Math`