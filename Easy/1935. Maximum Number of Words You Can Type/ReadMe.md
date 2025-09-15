# 1935. Maximum Number of Words You Can Type

**Difficulty:** Easy  
**Link:** [LeetCode 1935](https://leetcode.com/problems/maximum-number-of-words-you-can-type/)

---

## Problem Description
There is a malfunctioning keyboard with certain **broken letters**.  
You are given:
- A string `text` consisting of words separated by a single space.
- A string `brokenLetters` consisting of distinct lowercase letters.

A word cannot be typed if it contains at least one of the broken letters.  
Return the **number of words** you can still type using the keyboard.

---

## Example 1
**Input:**
text = "hello world"
brokenLetters = "ad"

makefile
Kodu kopyala

**Output:**
1

sql
Kodu kopyala
Explanation: Only `"world"` can be typed. `"hello"` contains `"a"` or `"d"`? No → but it contains `"h","e","l","o"` all fine. Actually `"hello"` contains no `"a"` or `"d"`, so it is typeable. `"world"` has `"d"`, so it cannot be typed.  
Correction → Final count = 1 (`"hello"`).  

---

## Example 2
**Input:**
```python
text = "leet code"
brokenLetters = "lt"
```

**Output:**
```python
1
```

Explanation: `"leet"` has `"l"`, `"t"` → broken. `"code"` is fine → only 1 word.

---

## Example 3
**Input:**
```python
text = "leet code"
brokenLetters = "e"
```

**Output:**
```python
0
```

Explanation: Both `"leet"` and `"code"` contain `"e"`. No word can be typed.

---

## Constraints
- `1 <= text.length <= 10^4`
- `0 <= brokenLetters.length <= 26`
- `text` consists of lowercase English letters and spaces.
- Words are separated by a single space, with no leading or trailing spaces.

---

## Approach

### Key Idea
- Preprocess `brokenLetters` into a set for O(1) membership tests.
- Split `text` into words.
- For each word, check if any letter belongs to the broken set:
  - If yes → skip.
  - If no → increment the count.

### Algorithm
1. Convert `brokenLetters` to a set → `broken`.
2. Split `text` into a list of words.
3. Initialize `count = 0`.
4. For each word:
   - If `not any(ch in broken for ch in word)` → `count += 1`.
5. Return `count`.

---

## Time and Space Complexity
- **Time Complexity:** O(n * m),  
  where n = number of words, m = average word length.  
- **Space Complexity:** O(k), where k = number of broken letters (≤ 26).

---

## Tags
`String`, `Set`, `Simulation`

---

## Notes
- Using `set(brokenLetters)` is crucial for efficiency.
- The solution is simple and readable, making it ideal for an **Easy**-level problem.