class Solution(object):
    def stringSequence(self, target):
        result = []
        current_string = ""
        for char in target:
            if not current_string:
                current_string = 'a'
                result.append(current_string)
            while current_string[-1] != char:
                current_string = current_string[:-1] + chr(ord(current_string[-1]) + 1)
                result.append(current_string)
            if current_string[-1] == char and len(current_string) < len(target):
                current_string += 'a'
                result.append(current_string)
        return result
solution = Solution()
print(solution.stringSequence("abc"))