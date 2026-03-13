# 3296. Minimum Number of Seconds to Make Mountain Height Zero

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 3296](https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/?)
 
# 🧠 Problem Description
# [Github LeetCode 3296. Minimum Number of Seconds to Make Mountain Height Zero](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3296.%20Minimum%20Number%20of%20Seconds%20to%20Make%20Mountain%20Height%20Zero)

class Solution:
    def minNumberOfSeconds(
        self, mountainHeight: int, workerTimes: List[int]
    ) -> int:
        maxWorkerTimes = max(workerTimes)
        l, r, ans = (
            1,
            maxWorkerTimes * mountainHeight * (mountainHeight + 1) // 2,
            0,
        )
        eps = 1e-7

        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for t in workerTimes:
                work = mid // t
                # find the largest k such that 1+2+...+k <= work
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2 + eps)
                cnt += k
            if cnt >= mountainHeight:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans