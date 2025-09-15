# 📘 LeetCode 1462 - Course Schedule IV

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1462](https://leetcode.com/problems/course-schedule-iv)

# 🧠 Problem Description 
# [Github LeetCode 1462 - Course Schedule IV](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1462.%20Course%20Schedule%20IV)

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            reachable[u][v] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
        result = []
        for u, v in queries:
            result.append(reachable[u][v])
        return result