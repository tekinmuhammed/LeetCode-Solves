# 3629. Minimum Jumps to Reach End via Prime Teleportation

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 3629](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/description/)

# 🧠 Problem Description 
# [Github LeetCode 3629. Minimum Jumps to Reach End via Prime Teleportation](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3629.%20Minimum%20Jumps%20to%20Reach%20End%20via%20Prime%20Teleportation) 

from collections import defaultdict
from typing import List

# Global Precomputation of prime factors using a Sieve
MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        edges = defaultdict(list)
        
        # Map primes to their indices
        for i, a in enumerate(nums):
            if len(factors[a]) == 1:
                edges[a].append(i)
                
        res = 0
        seen = [False] * n
        seen[-1] = True
        q = [n - 1]
        
        # BFS to find the shortest path
        while True:
            q2 = []
            for i in q:
                if i == 0:
                    return res
                
                # Check adjacent index (left)
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                    
                # Check adjacent index (right)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                    
                # Check teleportation via prime factors
                for p in factors[nums[i]]:
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    # Clear the edges to prevent redundant processing (O(N) guarantee)
                    edges[p].clear()
                    
            q = q2
            res += 1