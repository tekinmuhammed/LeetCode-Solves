# 1233. Remove Sub-Folders from the Filesystem

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 1233](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/)

# 🧠 Problem Description 
# [Github LeetCode 3136. Valid Word](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1233.%20Remove%20Sub-Folders%20from%20the%20Filesystem%20II)

class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        res = []
        for path in folder:
            if not res or not path.startswith(res[-1] + '/'):
                res.append(path)
        return res