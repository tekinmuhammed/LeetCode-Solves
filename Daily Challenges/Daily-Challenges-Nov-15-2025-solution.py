# 3234. Count the Number of Substrings With Dominant Ones — README

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3234](https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/description/)

# 🧠 Problem Description 
# [Github LeetCode 3234. Count the Number of Substrings With Dominant Ones — README](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3234.%20Count%20the%20Number%20of%20Substrings%20With%20Dominant%20Ones)

import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        B = int(math.sqrt(n)) + 1
        zero_indices = [-1]
        for i, char in enumerate(s):
            if char == '0':
                zero_indices.append(i)
        
        total_count = 0
        
        count_ones = 0
        for char in s:
            if char == '1':
                count_ones += 1
            else:
                total_count += count_ones * (count_ones + 1) // 2
                count_ones = 0
        total_count += count_ones * (count_ones + 1) // 2
        for i in range(1, len(zero_indices)):
            for j in range(i, min(len(zero_indices), i + B)):
                k = j - i + 1
                k_squared = k * k
                p_start = zero_indices[i]
                p_end = zero_indices[j]
                start_boundary = zero_indices[i-1] + 1
                end_boundary = n
                if j + 1 < len(zero_indices):
                    end_boundary = zero_indices[j+1]
                end_boundary -= 1
                
                N1_core = p_end - p_start + 1 - k
                N1_gerekli = k_squared - N1_core
                if N1_gerekli <= 0:
                    N1_gerekli = 0
                max_prefix_ones = p_start - start_boundary
                max_suffix_ones = end_boundary - p_end
                L_prefix_min = max(0, N1_gerekli - max_suffix_ones)
                L_prefix_max = min(max_prefix_ones, N1_gerekli)
                if N1_gerekli > max_prefix_ones + max_suffix_ones:
                    continue
                current_sub_count = 0
                for L_prefix in range(L_prefix_min, max_prefix_ones + 1):
                    L_suffix_min = max(0, N1_gerekli - L_prefix)
                    current_sub_count += (max_suffix_ones - L_suffix_min + 1)
                    
                total_count += current_sub_count

        return total_count