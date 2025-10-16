# 1792. Maximum Average Pass Ratio

# **Difficulty:** Medium  
# **Link:** [LeetCode 1792](https://leetcode.com/problems/maximum-average-pass-ratio/)

# 🧠 Problem Description 
# [Github LeetCode 1792. Maximum Average Pass Ratio](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1792.%20Maximum%20Average%20Pass%20Ratio-2)

import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """

        # (p+1)/(t+1) - p/t  -->  (t - p) / (t*(t+1))
        # float bölme zorunlu, yoksa Python2'de integer division olur.
        def gain(p, t):
            return (t - p) / float(t * (t + 1))

        # max-heap için kazancı negatifleyip koyuyoruz
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        total_ratio = sum(p / float(t) for _, p, t in heap)
        return total_ratio / len(classes)