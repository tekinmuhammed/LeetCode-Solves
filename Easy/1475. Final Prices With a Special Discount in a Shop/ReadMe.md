# 🟩 LeetCode 1475 - Final Prices With a Special Discount in a Shop

**Difficulty:** Easy  
**Problem Link:** [LeetCode 1475](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)

---

## 📘 Problem Description

You are given an array `prices` where `prices[i]` is the price of the `i-th` item in a shop.

The shop gives a **special discount** for each item. If there is a **next item** with a price less than or equal to the current item, you get a **discount equal to that next item's price**.

Return an array where `res[i]` is the **final price** of the `i-th` item after applying the discount (if any), otherwise leave it unchanged.

---

## 🧪 Example

### Input
```python
prices = [8, 4, 6, 2, 3]
```

### Output
```python
[4, 2, 4, 2, 3]
```

### Explanation:

- Item 0: Next smaller or equal is 4 → 8 - 4 = 4

- Item 1: Next smaller or equal is 2 → 4 - 2 = 2

- Item 2: Next smaller or equal is 2 → 6 - 2 = 4

- Item 3: Next smaller or equal is none → 2

- Item 4: No discount → 3

### 🚀 Approach

We can solve this efficiently using a `monotonic stack`:

- Iterate through the prices from left to right.

- Maintain a stack of indices where the discount hasn't been applied yet.

- For each current price:

- - While the top of the stack has a price `greater than or equal to` the current price, apply the discount.

- - Push the current index onto the stack.

-This ensures we find the `next smaller or equal` element efficiently.

### ⏱️ Complexity

- **Time Complexity:** `O(n)`

- - Each index is pushed and popped at most once.

- **Space Complexity:** `O(n)`

- - For the stack.

### 🏷️ Tags
`stack`, `monotonic stack`, `array`, `leetcode-easy`, `greedy`