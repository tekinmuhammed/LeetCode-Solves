# LeetCode 1106 - Parsing A Boolean Expression

## 🔗 Problem Link
[LeetCode 1106 - Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/)

## 🧠 Problem Description

Given a string expression representing a boolean expression, parse and evaluate its result.

Valid symbols include:
- `'t'` (true), `'f'` (false)
- `'!'` (NOT): e.g., `!(f)` → `true`
- `'&'` (AND): e.g., `&(t,f)` → `false`
- `'|'` (OR): e.g., `|(t,f)` → `true`

The expression will always be valid and properly formatted with parentheses.

## 🧪 Example

```python
Input: "&(|(!(f)))"
Output: True
```
## 💡 Approach

- Use a recursive parser to handle the expression tree.

- `!` applies `not` to a single expression.

- `&` applies `and` to multiple subexpressions.

- `|` applies `or` to multiple subexpressions.

- A helper function splits top-level comma-separated expressions within parentheses.

## 🧮 Complexity

**Time Complexity:** O(n)

**Space Complexity:** O(n) (due to recursion)

## 📌 Tags

`recursion`, `string-parsing`, `expression-evaluation`, `boolean-logic`, `DFS`