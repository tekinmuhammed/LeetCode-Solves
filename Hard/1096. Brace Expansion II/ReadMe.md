# 1096. Brace Expansion II

**Difficulty:** Hard 
**Problem Link:** [LeetCode 1096](https://leetcode.com/problems/brace-expansion-ii/description/)

---

## Problem
Under a grammar given below, strings can represent a set of lowercase words. Let's use `R(expr)` to denote the set of words the expression represents.

Grammar can best be understood through simple examples:
* Single letters represent a singleton set containing that word.
  * `R("a") = {"a"}`
  * `R("w") = {"w"}`
* When we take a comma-separated list of 2 or more expressions, we take the union of possibilities.
  * `R("{a,b,c}") = {"a","b","c"}`
  * `R("{{a,b},{b,c}}") = {"a","b","c"}` (Notice that duplicates are removed.)
* When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
  * `R("{a,b}{c,d}") = {"ac","ad","bc","bd"}`
  * `R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}`

Return the lexicographically sorted list of words that the expression represents.

---

# Approach

The structure of the expressions strictly follows a formal grammar. To parse and evaluate this cleanly, we can build a **Recursive Descent Parser**. We break the parsing logic into three distinct hierarchical levels, returning Python `set` objects at each level to automatically handle uniqueness.

1. **`expr()` (Expression - Handles Unions `,`)**:
   * An expression consists of one or more `term`s separated by commas.
   * It takes the union (`|`) of the sets returned by multiple `term()` calls.
2. **`term()` (Term - Handles Concatenations)**:
   * A term consists of one or more contiguous `item`s (e.g., `a{b,c}`).
   * It computes the Cartesian product (string concatenation) of the sets returned by contiguous `item()` calls. It starts with a base set `{""}` and iteratively builds combinations.
3. **`item()` (Item - Handles Base Cases and Groupings)**:
   * An item is either a single lowercase letter (which returns a singleton set like `{"a"}`) or a nested expression wrapped in braces `{...}`.
   * If it sees `{`, it consumes it, recursively calls `expr()` to evaluate everything inside, and then consumes the closing `}`.

By passing a global index pointer (`idx`) through these recursive functions, we parse the string in a single left-to-right pass. Finally, we convert the resulting set into a list and sort it lexicographically.

---

# Code

```python
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        idx = 0
        n = len(expression)

        def is_letter(c: str) -> bool:
            return "a" <= c <= "z"

        # Recursive descent parser
        def expr() -> set:
            nonlocal idx
            ret = set()
            while True:
                # Take the union with the result of term()
                ret |= term()
                # Continue if a comma is matched; otherwise, stop matching
                if idx < n and expression[idx] == ",":
                    idx += 1
                    continue
                else:
                    break
            return ret

        # term -> item | item term
        def term() -> set:
            nonlocal idx
            # Initialize an empty set and take its Cartesian product with subsequent results
            ret = {""}
            # An item starts with { or a lowercase letter; continue matching only when this condition is met
            while idx < n and (
                expression[idx] == "{" or is_letter(expression[idx])
            ):
                sub = item()
                tmp = set()
                for left in ret:
                    for right in sub:
                        tmp.add(left + right)
                ret = tmp
            return ret

        # item -> letter | { expr }
        def item() -> set:
            nonlocal idx
            ret = set()
            if expression[idx] == "{":
                idx += 1
                ret = expr()
            else:
                ret = {expression[idx]}
            idx += 1
            return ret

        ret = expr()
        return sorted(list(ret))
```

---

# Example Walkthrough

Let's trace the parsing of `"{a,b}c"`:

1. **`expr()`** is called at `idx = 0`.
   * Enters loop, calls **`term()`**.
2. **`term()`** initializes `ret = {""}`.
   * Sees `{` at `idx = 0`. Calls **`item()`**.
   * **`item()`** sees `{`, skips it (`idx=1`), calls **`expr()`**.
     * Inner **`expr()`** calls **`term()`** for `a`. Returns `{"a"}`.
     * Inner **`expr()`** sees `,`, skips it, calls **`term()`** for `b`. Returns `{"b"}`.
     * Inner **`expr()`** takes union $\rightarrow$ `{"a", "b"}`. Returns.
   * **`item()`** skips `}` at `idx=4`. Returns `{"a", "b"}` to `term()`.
   * **`term()`** updates `ret` via Cartesian product: `ret = {"a", "b"}`.
   * Next iteration in `term()` loop sees `c` at `idx=5`. Calls **`item()`**.
   * **`item()`** sees letter `c`. Returns `{"c"}`. `idx=6`.
   * **`term()`** applies Cartesian product between `{"a", "b"}` and `{"c"}` $\rightarrow$ `{"ac", "bc"}`.
   * `term()` loop ends, returns `{"ac", "bc"}` to outer `expr()`.
3. Outer **`expr()`** sees end of string, breaks loop, returns `{"ac", "bc"}`.
4. Main function sorts the result $\rightarrow$ `["ac", "bc"]`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(2^M)$ in the worst case, where $M$ is related to the number of comma-separated groups. Because expressions like `{a,b}{c,d}{e,f}...` generate the Cartesian product, the number of generated strings grows exponentially. String concatenation and sorting also add overhead, making the time complexity heavily dependent on the output size. The recursive parsing itself takes linear time relative to the number of characters, but the set operations dominate.

Space Complexity

$\mathcal{O}(2^M)$

The space complexity is dominated by the storage required for the final generated strings (and intermediate sets during the Cartesian product phase), which can grow exponentially. The recursion stack depth is limited by the maximum nesting depth of the braces, which is at most $\mathcal{O}(N)$ where $N$ is the length of the string.