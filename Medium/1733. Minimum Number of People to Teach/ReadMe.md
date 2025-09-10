# 1733. Minimum Number of People to Teach

**Difficulty:** Medium  
**Link:** [LeetCode 1733](https://leetcode.com/problems/minimum-number-of-people-to-teach/)

---

## Problem Description
You are given:
- `n` languages, numbered `1..n`.
- `languages[i]`: the set of languages spoken by the i-th person.
- `friendships`: a list of pairs `[u, v]` indicating that `u` and `v` are friends.

Two friends can communicate if they share at least one common language.

Your task is to find the **minimum number of people** you need to teach **a single new language** so that every pair of friends can communicate.

---

## Example 1
**Input:**
```python
n = 2
languages = [[1], [2], [1,2]]
friendships = [[1,2], [1,3], [2,3]]
```

**Output:**
```python
1
```

**Explanation:**
- Person 1 knows `{1}`, Person 2 knows `{2}`, Person 3 knows `{1,2}`.  
- Friendship `(1,2)` cannot communicate.  
- If we teach person 1 or person 2 the other language, everyone can communicate.  

---

## Example 2
**Input:**
```python
n = 3
languages = [[2], [1,3], [1,2], [3]]
friendships = [[1,4], [1,2], [3,4], [2,3]]
```

**Output:**
```python
2
```

---

## Constraints
- `2 <= n <= 500`
- `languages.length == m` where `m` is the number of people
- `1 <= languages[i].length <= n`
- `friendships.length <= 10^4`
- Friendship pairs are unique and `1 <= u, v <= m`

---

## Approach

### Key Idea
- Identify which friendships cannot communicate (`langs[u] ∩ langs[v] == ∅`).  
- Collect all such people into a set `need_teach`.  
- For each language `1..n`, count how many in `need_teach` **do not** know that language.  
- The minimum count is the answer.

### Algorithm
1. Convert each `languages[i]` list into a `set` for fast lookup.  
2. Traverse friendships:
   - If two friends share no common language, add both to `need_teach`.  
3. If `need_teach` is empty → return `0`.  
4. For each possible language `lang`:
   - Count how many in `need_teach` lack `lang`.  
   - Track the minimum across all languages.  
5. Return this minimum.

---

## Time and Space Complexity
- **Time Complexity:**  
  - Friendship check: O(F * L) in worst case (F = friendships, L = avg. language count).  
  - Language evaluation: O(n * |need_teach|).  
  - Efficient enough for given constraints.  

- **Space Complexity:** O(m * L) for storing language sets.

---

## Tags
HashSet, Greedy, Simulation, Graph

---

## Notes
- Only **one language** can be taught.  
- The trick is focusing only on people in `need_teach` (those in problematic friendships), not everyone.
👉 İster 