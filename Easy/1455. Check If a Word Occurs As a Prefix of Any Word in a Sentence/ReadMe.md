# 📝 LeetCode 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1455](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence)

---

## 📘 Problem Description

Given a sentence that consists of words separated by spaces, return the **1-based index** of the first word that starts with `searchWord`.

If no such word exists, return `-1`.

---

## 🧪 Example

### Input:
```python
sentence = "i love eating burger"
searchWord = "burg"
```

## Output:
```python
4
```

## Explanation:

The 4th word `"burger"` starts with `"burg"`.

## 🚀 Approach

- Split the sentence into a list of words using `split()`.

- Loop through each word and check if it starts with the given `searchWord`.

- If yes, return the **1-based index** of that word.

- If no match is found after the loop, return `-1`.

## ⏱️ Complexity

- **Time Complexity:** `O(n)`, where `n` is the number of characters in the sentence.

- **Space Complexity:** `O(w)`, where `w` is the number of words in the sentence.

## 🏷️ Tags
`string`, `prefix`, `split`, `linear-search`, `leetcode-easy`