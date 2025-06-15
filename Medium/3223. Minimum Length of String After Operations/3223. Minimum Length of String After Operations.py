class Solution:
    def minimumLength(self, s: str) -> int:
        f = collections.Counter(s)
        for k in f.keys():
            while f[k] >= 3:
                f[k] -= 2
        return sum(f.values())