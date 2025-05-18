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