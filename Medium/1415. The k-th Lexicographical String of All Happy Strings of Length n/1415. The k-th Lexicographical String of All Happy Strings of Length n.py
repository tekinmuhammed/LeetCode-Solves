class Solution(object):
    def getHappyString(self, n, k):
        res = []

        def dfs(path):
            if len(res) >= k:
                return
            if len(path) == n:
                res.append(path)
                return

            for c in ['a', 'b', 'c']:
                if not path or path[-1] != c:
                    dfs(path + c)

        dfs("")
        
        if len(res) < k:
            return ""
        return res[k-1]