# 🧩 3003. Maximize the Number of Partitions After Operations

# **Difficulty:** Hard
# **Problem Link:** [LeetCode 3003](https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/description/)

# 🧠 Problem Description
# [Github LeetCode 3003. Maximize the Number of Partitions After Operations](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/3003.%20Maximize%20the%20Number%20of%20Partitions%20After%20Operations)

import functools

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        @functools.lru_cache(None)
        def dp(i: int, can_change: bool, mask: int) -> int:
            if i == n:
                return 0
            bit_cur_char = 1 << (ord(s[i]) - ord('a'))
            new_mask = mask | bit_cur_char
            
            res = 0
            
            if new_mask.bit_count() > k:
                res = 1 + dp(i + 1, can_change, bit_cur_char)
            else:
                res = dp(i + 1, can_change, new_mask)
            if can_change:
                for j in range(26):
                    bit_brute_char = 1 << j
                    new_mask_changed = mask | bit_brute_char

                    if new_mask_changed.bit_count() > k:
                        res = max(res, 1 + dp(i + 1, False, bit_brute_char))
                    else:
                        res = max(res, dp(i + 1, False, new_mask_changed))

            return res
        return dp(0, True, 0) + 1    