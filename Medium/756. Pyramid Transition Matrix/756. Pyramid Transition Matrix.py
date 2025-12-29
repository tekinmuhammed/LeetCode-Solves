class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        from collections import defaultdict

        # Build mapping: (left, right) -> possible tops
        mp = defaultdict(list)
        for a in allowed:
            mp[a[0] + a[1]].append(a[2])

        memo = set()

        def dfs(curr):
            if len(curr) == 1:
                return True
            if curr in memo:
                return False

            def build_next(i, path):
                if i == len(curr) - 1:
                    return dfs(path)

                key = curr[i] + curr[i + 1]
                if key not in mp:
                    return False

                for c in mp[key]:
                    if build_next(i + 1, path + c):
                        return True
                return False

            if not build_next(0, ""):
                memo.add(curr)
                return False
            return True

        return dfs(bottom)