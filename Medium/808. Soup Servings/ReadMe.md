# LeetCode 808 - Soup Servings

## 📝 Problem Description

We have two types of soup: **A** and **B**. Initially, each soup has `n` milliliters. There are four serving operations:

1. Serve 100 ml of soup A and 0 ml of soup B  
2. Serve 75 ml of soup A and 25 ml of soup B  
3. Serve 50 ml of soup A and 50 ml of soup B  
4. Serve 25 ml of soup A and 75 ml of soup B  

When we serve some soup, we **reduce its amount** by the given milliliters (but not below zero). The process stops when **either soup A or soup B** becomes empty.

We want to calculate the **probability** that **soup A becomes empty first** **plus half the probability** that **both become empty at the same time**.

If `n` is very large, the answer approaches 1.

---

## 💡 Example

### Input
```python
n = 50
```

### Output
```python
0.625
```

### 📊 Complexity
- **Time Complexity:** `O((n/25)^2)`

- - We scale `n` down by 25 for DP states, then fill an `m x m` table.

- **Space Complexity:** `O((n/25)^2)`

- - Stores results for each `(i, j)` state.

### ✅ Key Points

- `n` is scaled down by `25` since all serving amounts are multiples of `25 ml`.

- Dynamic Programming memoizes probabilities for `(i, j)` soup states.

- Early stopping optimization: if probability is > `1 - 1e-5`, we directly return `1`.