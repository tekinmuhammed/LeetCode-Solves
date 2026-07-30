# 3014. Minimum Number of Pushes to Type Word I

**Difficulty:** Easy
**Problem Link:** [LeetCode 3014](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/)

---

## Problem
You are given a string `word` containing **distinct** lowercase English letters. 

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key `2` is mapped with `["a","b","c"]`, we need to push the key one time to type `"a"`, two times to type `"b"`, and three times to type `"c"`. 

It is allowed to remap the keys numbered `2` to `9` to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string `word`.

---

# Approach

Since the problem guarantees that all letters in the `word` are **distinct**, we don't need to worry about letter frequencies (which is required in Part II of this problem). We just need to assign the letters greedily to the available 8 keys (`2` through `9`).

To minimize the total pushes:
1. The first 8 letters of the word should be placed at the first position of the 8 keys. These will require **1 push** each.
2. The next 8 letters (if the word is longer than 8 characters) should be placed at the second position of the 8 keys. These will require **2 pushes** each.
3. The next 8 letters will require **3 pushes** each, and so on.

Using Python, we can calculate this in a single line. For a character at index `i` (0-indexed), its push cost is `(i // 8) + 1`. We simply sum this cost for all characters in the string.

---

# Code

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(i // 8 + 1 for i in range(len(word)))
```

---

# Example Walkthrough

Example: `word = "abcdefghi"` (Length = 9)

We have 8 keys available (2, 3, 4, 5, 6, 7, 8, 9). 

1. **Indices 0 to 7 ("abcdefgh")**:
   * These 8 letters can each be assigned as the 1st letter on the 8 keys.
   * Math: `0 // 8 + 1` = 1, `7 // 8 + 1` = 1.
   * Cost = 8 * 1 = 8 pushes.

2. **Index 8 ("i")**:
   * All 1st positions are taken. This letter must be the 2nd letter on one of the keys.
   * Math: `8 // 8 + 1` = 2.
   * Cost = 1 * 2 = 2 pushes.

**Total Pushes**: 8 + 2 = 10.

---

# Complexity Analysis

Time Complexity

O(N)

Where N is the length of the string `word`. We iterate through the string's length exactly once to compute the sum. 
*(Note: Because the maximum length of `word` is 26 since all characters are distinct, this actually runs in O(1) constant time as an upper bound).*

Space Complexity

O(1)

The space used does not scale with the input size. The algorithm only computes mathematical operations based on indices, requiring no extra memory.