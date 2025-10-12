# 2163. Minimum Difference in Sums After Removal of Elements

# **Difficulty:** Hard  
# **Problem Link:** [LeetCode 2163](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/)

# 🧠 Problem Description 
# [Github LeetCode 3136. Valid Word](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2163.%20Minimum%20Difference%20in%20Sums%20After%20Removal%20of%20Elements)

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n3, n = len(nums), len(nums) // 3

        part1 = [0] * (n + 1)
        # max heap
        total = sum(nums[:n])
        ql = [-x for x in nums[:n]]
        heapq.heapify(ql)
        part1[0] = total

        for i in range(n, n * 2):
            total += nums[i]
            heapq.heappush(ql, -nums[i])
            total -= -heapq.heappop(ql)
            part1[i - (n - 1)] = total

        # min heap
        part2 = sum(nums[n * 2 :])
        qr = nums[n * 2 :]
        heapq.heapify(qr)
        ans = part1[n] - part2

        for i in range(n * 2 - 1, n - 1, -1):
            part2 += nums[i]
            heapq.heappush(qr, nums[i])
            part2 -= heapq.heappop(qr)
            ans = min(ans, part1[i - n] - part2)

        return ans