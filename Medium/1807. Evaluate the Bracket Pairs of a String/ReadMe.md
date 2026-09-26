# 1807. Evaluate the Bracket Pairs of a String

**Difficulty:** Medium 
**Problem Link:** [LeetCode 1807](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/)

---

## Problem
You are given a string `s` that contains some bracket pairs, with each pair containing a non-empty key. You are also given a 2D string array `knowledge` where each element is `[key, value]`.

You need to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key `k`:
* If `k` is in `knowledge`, replace the bracket pair and the key with its corresponding `value`.
* If `k` is not in `knowledge`, replace the bracket pair and the key with a question mark `"?"`.

Each bracket pair will contain exactly one key, and they are not nested. Return the resulting string after evaluating all of the bracket pairs.

Example:

Input  
s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]  

Output  
"bobistwoyearsold"

---

# Approach

To solve this efficiently without repeatedly searching or creating multiple intermediate strings, we can use a **Hash Map** combined with **Single-Pass Parsing**.

Steps:
1. **Hash Map Conversion**: Convert the `knowledge` list into a dictionary (`d = dict(knowledge)`). This allows us to look up keys in $\mathcal{O}(1)$ average time.
2. **String Builder**: Use a list `ans` to build the final string. In Python, appending to a list and then using `"".join()` is much faster and more memory-efficient than repeatedly concatenating strings using `+`.
3. **Tracking State**: Use a variable `start` to track whether we are currently inside a bracket pair. We initialize `start = -1` (meaning we are outside).
4. **Single Pass**: Iterate through the string `s` character by character along with its index `i`:
   * If the character is `'('`, we mark the start of a key by setting `start = i`.
   * If the character is `')'`, we have reached the end of a key. We extract the key using string slicing `s[start + 1 : i]`. We fetch its value from our dictionary using `d.get(key, "?")` which automatically handles missing keys by returning `"?"`. We append this value to `ans` and reset `start = -1`.
   * If the character is a regular letter (checked by `start < 0`), we simply append it to `ans`.
5. **Join and Return**: Finally, combine all pieces in the `ans` list into a single string and return it.

---

# Code

```python
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Convert knowledge to a dictionary for O(1) lookups
        d = dict(knowledge)
        ans, start = [], -1
        
        for i, c in enumerate(s):
            if c == "(":
                # Mark the beginning of a key
                start = i
            elif c == ")":
                # Extract the key, look it up, append result, and reset state
                ans.append(d.get(s[start + 1 : i], "?"))
                start = -1
            elif start < 0:
                # If we are outside a bracket, just append the character
                ans.append(c)
                
        return "".join(ans)
```

---

# Example Walkthrough

Let's trace `s = "(a)b(c)"` and `knowledge = [["a", "x"]]`

1. **Initialization**: 
   * `d = {"a": "x"}`
   * `ans = []`, `start = -1`

2. **Iteration**:
   * `i = 0, c = '('` $\rightarrow$ set `start = 0`. `ans = []`
   * `i = 1, c = 'a'` $\rightarrow$ `start` is 0 (not < 0), do nothing. `ans = []`
   * `i = 2, c = ')'` $\rightarrow$ extract key `s[1:2]` which is `"a"`. Lookup `"a"` in `d` gets `"x"`. Append `"x"` to `ans`. Reset `start = -1`. `ans = ["x"]`
   * `i = 3, c = 'b'` $\rightarrow$ `start < 0`, append `'b'`. `ans = ["x", "b"]`
   * `i = 4, c = '('` $\rightarrow$ set `start = 4`. `ans = ["x", "b"]`
   * `i = 5, c = 'c'` $\rightarrow$ `start` is 4, do nothing.
   * `i = 6, c = ')'` $\rightarrow$ extract key `s[5:6]` which is `"c"`. Lookup `"c"` in `d` gets `"?"` (not found). Append `"?"` to `ans`. Reset `start = -1`. `ans = ["x", "b", "?"]`

3. **Result**: `"".join(ans)` returns `"xb?"`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N + K)$

Where $N$ is the length of the string `s` and $K$ is the total number of characters across all keys and values in the `knowledge` array. Building the dictionary takes $\mathcal{O}(K)$ time. Iterating through the string `s` and extracting slices takes $\mathcal{O}(N)$ time.

Space Complexity

$\mathcal{O}(N + K)$

The dictionary `d` requires $\mathcal{O}(K)$ space to store all key-value pairs. The `ans` array will store the resulting string components, which takes $\mathcal{O}(N)$ space in the worst case.