# LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen

# 🔗 Problem Link 
#[LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen](https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/)

# 🧠 Problem Description
#[Github LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/3324.%20Find%20the%20Sequence%20of%20Strings%20Appeared%20on%20the%20Screen)

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