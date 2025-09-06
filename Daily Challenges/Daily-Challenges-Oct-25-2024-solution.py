# 🗂️ LeetCode 1233 - Remove Sub-Folders from the Filesystem

#**Difficulty:** Medium  
#**Problem Link:** 
#[LeetCode 1233](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem)

# 🧠 Problem Description
#[Github LeetCode 1233. Remove Sub-Folders from the Filesystem](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1233.%20Remove%20Sub-Folders%20from%20the%20Filesystem)


class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort()

        result = []
        previous = " "

        for f in folder:
            if not f.startswith(previous):
                result.append(f)
                previous = f + "/"
        return result
solution = Solution()
folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
print(solution.removeSubfolders(folder))  