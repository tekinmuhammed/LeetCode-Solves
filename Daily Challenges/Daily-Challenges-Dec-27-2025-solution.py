# 2402. Meeting Rooms III

# **Difficulty:** Hard  
# **Link:** [LeetCode 2402](https://leetcode.com/problems/meeting-rooms-iii)

# 🧠 Problem Description
# [Github LeetCode 2402. Meeting Rooms III](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/2402.%20Meeting%20Rooms%20III-2)

class Solution:
    def mostBooked(self, n, meetings):
        ans = [0] * n
        times = [0] * n
        meetings.sort()

        for meeting in meetings:
            start, end = meeting
            flag = False
            minind = -1
            val = float('inf')
            for j in range(n):
                if times[j] < val:
                    val = times[j]
                    minind = j
                if times[j] <= start:
                    flag = True
                    ans[j] += 1
                    times[j] = end
                    break
            if not flag:
                ans[minind] += 1
                times[minind] += (end - start)

        maxi = -1
        id = -1
        for i in range(n):
            if ans[i] > maxi:
                maxi = ans[i]
                id = i

        return id