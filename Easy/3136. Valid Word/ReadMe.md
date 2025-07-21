# 3136. Valid Word

**Difficulty:** Easy  
**Link:** [LeetCode 3136](https://leetcode.com/problems/valid-word)

---

## Problem Description

A string `word` is called **valid** if:

1. It has **at least 3 characters**.
2. It consists of **only letters and digits**.
3. It contains **at least one vowel**.
4. It contains **at least one consonant**.

Write a function that returns `True` if the word is valid according to the above rules, and `False` otherwise.

---

## Example

### Input
```python
word = "a1b"
```

### Output
```python
True
```

### Explanation

- Length is 3 ✅

- Contains only alphanumeric characters ✅

- Contains vowel 'a' ✅

- Contains consonant 'b' ✅

### Constraints

- The input string contains only ASCII characters.

### Approach & Explanation

The function performs the following checks in order:

1. **Length Check:** If the word has fewer than 3 characters → `False`.

2. **Character Check:** If any character is not a letter or digit → `False`.

3. **Vowel and Consonant Check:** Track presence of both using flags while iterating.

- - Define a vowel set: `aeiouAEIOU`

- - Any alphabetic character not in vowels is a consonant.

The word is valid if all conditions are satisfied.

### Time and Space Complexity

- **Time Complexity:** `O(n)`, where `n` is the length of the word.

- **Space Complexity:** `O(1)`, since we only use constant space for tracking flags and character sets.

### Tags

`String`, `Validation`, `Set`, `Simulation`

### Summary

This problem focuses on string validation using simple character checks and logical conditions.
It's a good exercise for beginners working with string parsing and condition logic.