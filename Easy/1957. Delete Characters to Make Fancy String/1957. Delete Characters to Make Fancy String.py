class Solution(object):
    def makeFancyString(self, s):
        result = []

        for char in s:
            if len(result) < 2 or not (result[-1] == result[-2] == char):
                result.append(char)
        return ''.join(result)
solution = Solution()
s = "leeetcode"
print(solution.makeFancyString(s))