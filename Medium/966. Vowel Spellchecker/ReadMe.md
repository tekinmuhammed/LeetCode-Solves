# 966. Vowel Spellchecker

**Difficulty:** Medium  
**Link:** [LeetCode 966](https://leetcode.com/problems/vowel-spellchecker/)

---

## Problem Description
Given a `wordlist`, implement a spellchecker for queries that returns the word from the `wordlist` according to the following priority rules:

1. **Exact Match (case-sensitive)**  
   If the query matches exactly with a word in `wordlist`, return the same word.

2. **Case-Insensitive Match**  
   If not exact, but query matches ignoring capitalization, return the first such word from `wordlist`.

3. **Vowel Error Match**  
   If not case-insensitive, replace all vowels (`a, e, i, o, u`) in both the query and words with `*`.  
   If they match, return the first such word from `wordlist`.

4. **No Match**  
   If none of the above match, return `""`.

---

## Example 1
**Input:**
```python
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
```

**Output:**
```python
["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
```

---

## Constraints
- `1 <= wordlist.length, queries.length <= 5000`
- `1 <= wordlist[i].length, queries[i].length <= 7`
- Each word consists only of English letters.

---

## Approach

### Key Idea
Use three levels of lookup tables to ensure O(1) query resolution:
- `words_perfect`: set for exact matches.
- `words_case`: dictionary for first occurrence of lowercase forms.
- `words_vowel`: dictionary for vowel-masked forms.

### Algorithm
1. Preprocess `wordlist` into three structures:
   - `set` for perfect matches.
   - `dict` mapping lowercase → original word.
   - `dict` mapping "devoweled" form → original word.
2. For each query:
   - If in `words_perfect`, return as is.
   - Else if lowercase query in `words_case`, return mapped word.
   - Else if vowel-masked query in `words_vowel`, return mapped word.
   - Otherwise return `""`.

---

## Time and Space Complexity
- **Preprocessing:** O(n * k), where n = `len(wordlist)`, k = max word length.
- **Query Handling:** O(m * k), where m = `len(queries)`.  
- **Total Complexity:** O((n + m) * k)
- **Space Complexity:** O(n * k) for the lookup tables.

---

## Tags
`Hash-Table`, `String`, `Preprocessing`

---

## Notes
- Only the **first occurrence** in `wordlist` counts for case-insensitive and vowel-error matches.  
- Vowel replacement uses `*` but any placeholder could be used.  
- Order of rules is strict — once a match is found, no need to check others.