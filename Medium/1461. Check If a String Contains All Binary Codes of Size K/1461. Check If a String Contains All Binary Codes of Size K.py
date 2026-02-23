class Solution(object):
    def hasAllCodes(self, s, k):
        need = 1 << k          # total binary codes
        seen = set()

        num = 0
        mask = need - 1        # keep last k bits

        for i in range(len(s)):
            num = ((num << 1) & mask) | int(s[i])

            if i >= k - 1:
                seen.add(num)
                if len(seen) == need:
                    return True

        return False