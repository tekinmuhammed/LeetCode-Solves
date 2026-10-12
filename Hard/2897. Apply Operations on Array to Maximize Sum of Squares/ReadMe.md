# 2897. Apply Operations on Array to Maximize Sum of Squares

**Difficulty:** Medium  
**Problem Link:** [LeetCode 2897](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/description/)

---

## Problem
You are given a 0-indexed integer array `nums` and a positive integer `k`.

You can do the following operation on the array any number of times:
* Choose any two indices `i` and `j` such that `i != j`, and replace `nums[i]` and `nums[j]` with `(nums[i] AND nums[j])` and `(nums[i] OR nums[j])` respectively, where `AND` is the bitwise AND operation and `OR` is the bitwise OR operation.

Return the **maximum possible sum of squares** of `k` elements selected from `nums` after applying the operation any number of times. Since the answer can be very large, return it modulo $10^9 + 7$.

---

# Approach

The bitwise operations `AND` and `OR` are bit-preserving. When applied to any two numbers, they do not create or destroy any bits; they merely **re-distribute** the bits between the two numbers. 

To maximize the sum of squares $\sum (num)^2$, a mathematical property comes into play: **clustering values is always better than distributing them evenly**. For example, $5^2 + 1^2 = 26$, whereas $6^2 + 0^2 = 36$. To maximize the sum of squares, we want to make a few numbers as large as possible rather than having many moderately sized numbers.

Using the bit-preservation property, we can think of all numbers in the array as a shared pool of bits. We can shift bits around so that the largest possible numbers are concentrated into our choice of `k` elements.

Steps:
1. **Bit Counting**: Since the numbers are within standard constraints (up to $10^9$, which fits well within 30 bits), we can count how many numbers have a `1` bit set at each bit position from `0` to `29`.
2. **Greedy Reconstruction**: We want to pick `k` numbers. To maximize their squares, we want the most significant bits to be concentrated as heavily as possible. We run a loop `k` times to build `k` distinct numbers.
3. **Building Each Number**: For each of the `k` numbers, we iterate from the highest bit position ($29$) down to $0$. If there is at least one available `1` bit in our global counter (`cnt[j] > 0`), we set that bit in our current number (`cur`) and decrement the global counter.
4. **Sum of Squares**: Square each constructed number, add it to our running total modulo $10^9 + 7$, and return the final result.

---

# Code

```python
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 30

        # Count the number of 1 bits at each position across all numbers
        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    cnt[i] += 1

        res = 0
        for _ in range(k):
            cur = 0
            # Construct the current number from the most significant bit to the least significant bit
            for j in range(29, -1, -1):
                if cnt[j] > 0:
                    cur |= 1 << j
                    cnt[j] -= 1
            res = (res + cur * cur) % MOD

        return res
```

---

# Example Walkthrough

Let's trace `nums = [2, 6, 5]`, `k = 2`.
Binary representations:
* `2` = `010` (bit 1 is set)
* `6` = `110` (bits 2 and 1 are set)
* `5` = `101` (bits 2 and 0 are set)

1. **Bit Counts (`cnt`)**:
   * Bit 2: 2 (from 6 and 5)
   * Bit 1: 2 (from 2 and 6)
   * Bit 0: 1 (from 5)
   *(Other higher bits are 0)*

2. **First Number Construction (`_ = 0`)**:
   * Check bit 2: `cnt[2] > 0` $\rightarrow$ set bit 2 (`cur |= 4`), `cnt[2]` becomes 1.
   * Check bit 1: `cnt[1] > 0` $\rightarrow$ set bit 1 (`cur |= 2`), `cnt[1]` becomes 1.
   * Check bit 0: `cnt[0] > 0` $\rightarrow$ set bit 0 (`cur |= 1`), `cnt[0]` becomes 0.
   * First number `cur` = `4 + 2 + 1 = 7` (Binary `111`).
   * Add square to result: `res = 7 * 7 = 49`.

3. **Second Number Construction (`_ = 1`)**:
   * Check bit 2: `cnt[2] > 0` $\rightarrow$ set bit 2 (`cur |= 4`), `cnt[2]` becomes 0.
   * Check bit 1: `cnt[1] > 0` $\rightarrow$ set bit 1 (`cur |= 2`), `cnt[1]` becomes 0.
   * Check bit 0: `cnt[0] == 0` $\rightarrow$ skip.
   * Second number `cur` = `4 + 2 = 6` (Binary `110`).
   * Add square to result: `res = (49 + 6 * 6) % MOD = (49 + 36) = 85`.

Result: `85`.

---

# Complexity Analysis

Time Complexity

$\mathcal{O}(N + K \cdot B)$

Where $N$ is the number of elements in `nums`, $K$ is the number of elements to pick, and $B$ is the number of bit positions (which is 30). Counting the bits takes $\mathcal{O}(N \cdot B)$ time. Constructing the `k` numbers takes $\mathcal{O}(K \cdot B)$ time. Since $B = 30$ is a small constant, this simplifies to $\mathcal{O}(N + K)$, making it extremely efficient.

Space Complexity

$\mathcal{O}(B)$

We use a constant-sized array `cnt` of length 30 to store the bit counts. No additional memory that scales with the input array size is required, yielding $\mathcal{O}(1)$ auxiliary space.