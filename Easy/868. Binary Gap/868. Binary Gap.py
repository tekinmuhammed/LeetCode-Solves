class Solution(object):
    def binaryGap(self, n):
        b = bin(n)[2:]   # binary string
        last = -1
        max_gap = 0

        for i in range(len(b)):
            if b[i] == '1':
                if last != -1:
                    max_gap = max(max_gap, i - last)
                last = i

        return max_gap