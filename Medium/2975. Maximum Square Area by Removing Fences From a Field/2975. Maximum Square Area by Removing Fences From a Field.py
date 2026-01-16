class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7

        # Add fixed boundary fences
        h = sorted([1] + hFences + [m])
        v = sorted([1] + vFences + [n])

        # All possible horizontal gaps
        h_gaps = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_gaps.add(h[j] - h[i])

        # All possible vertical gaps
        v_gaps = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_gaps.add(v[j] - v[i])

        # Find common gaps
        common = h_gaps & v_gaps
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD