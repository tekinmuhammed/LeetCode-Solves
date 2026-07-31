# 3016. Minimum Number of Pushes to Type Word II

**Difficulty:** Medium
**Problem Link:** [LeetCode 3016](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/)

---
 
## Problem 
You are given a string `word` containing lowercase English letters. 

Unlike Part I, the letters in the string are **not necessarily distinct**. You have 8 keys available on a telephone keypad (numbered `2` to `9`). You can remap these keys to any amount of letters, but each letter must be mapped to exactly one key.  
 
You need to find the minimum number of times the keys will be pushed to type the string `word`. 
 
Example: 
 
Input   
word = "abcde"  
 
Output   
5   
   
Input   
word = "aabbccddeeffgghhiiiiii"   
 
Output   
24   
 
--- 
 
# Approach 

Since characters can appear multiple times, we must prioritize the most frequently used characters. The goal is to assign the characters that appear most often to the first position of a key (requiring 1 push), the next most frequent to the second position (requiring 2 pushes), and so on. 
 
This is a classic **Greedy Algorithm**. 
 
Steps: 
1. **Count Frequencies**: Create an array of size 26 to store the frequency of each lowercase letter in the string.
2. **Sort**: Sort the frequency array in descending order. We don't care which letter has which frequency; we only care about processing the highest frequencies first.
3. **Assign and Calculate**: Iterate through the sorted frequencies. 
   * The first 8 highest frequencies are placed at position 1 on the 8 available keys (cost = `1 * frequency`).
   * The next 8 highest frequencies are placed at position 2 (cost = `2 * frequency`).
   * We calculate the multiplier using `(i // 8) + 1` where `i` is the index of the sorted array.
4. **Early Exit**: If we encounter a frequency of `0`, we can break out of the loop early since all remaining frequencies will also be `0`.
 
--- 
 
# Code 

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        # frequency list to store count of each letter
        frequency = [0] * 26

        # Count occurrences of each letter
        for c in word:
            frequency[ord(c) - ord("a")] += 1
        # sort frequencies in descending order 
        frequency.sort(reverse=True)

        total_pushes = 0

        # calculate total number of presses
        for i in range(26):
            if frequency[i] == 0:
                break
            total_pushes += (i // 8 + 1) * frequency[i]

        return total_pushes
```

---

# Example Walkthrough

Let's say `word = "aaabbbcccdddeeefffggghhh"`

1. **Frequencies**: We have 8 distinct letters, each appearing 3 times
   `frequency` (sorted) = `[3, 3, 3, 3, 3, 3, 3, 3, 0, 0, ...]`
2. **First 8 letters (indices 0 to 7)**:
   * Multiplier: `i // 8 + 1` = `1`
   * We have 8 keys. Each key gets one of these letters at the first position
   * Total for these: `8 letters * 3 occurrences * 1 push = 24 pushes`
3. **Index 8 (frequency is 0)**:
   * Loop breaks

Result: `24`

If we had a 9th letter, say "i" appearing 2 times, its index would be 8. Its cost would be `(8 // 8 + 1) = 2` pushes per occurrence. So, `2 * 2 = 4` additional pushes.

---

# Complexity Analysis

Time Complexity

O(N)

Where N is the length of the string `word`. 
- Counting the characters takes O(N) time.
- Sorting the frequency array of size 26 takes O(26 log 26) which is O(1) constant time.
- The final loop runs at most 26 times, which is also O(1) constant time.
Overall, the time complexity is strictly linear with respect to the input length.

Space Complexity

O(1)

The space used is an array of exactly 26 integers to store character frequencies. Since this size is fixed and does not grow with the size of the input string `word`, the space complexity is O(1).