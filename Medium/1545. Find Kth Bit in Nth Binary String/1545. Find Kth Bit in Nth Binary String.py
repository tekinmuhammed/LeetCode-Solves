class Solution(object):
    def findKthBit(self, n, k):
        def invert(s):
            return ''.join('1' if char == '0' else '0' for char in s)

        def generateSn(n):
            if n == 1:
                return "0"
            prev = generateSn(n - 1)
            return prev + "1" + invert(prev)[::-1]

        sn = generateSn(n)
        return sn[k - 1]

solution = Solution()
n = 3
k = 1

print(solution.findKthBit(n, k))
