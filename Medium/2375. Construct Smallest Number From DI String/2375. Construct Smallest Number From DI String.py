class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        stack = []
        result = []
        num = 1
        for char in pattern + "I":
            stack.append(str(num))
            num += 1
            if char == "I":
                while stack:
                    result.append(stack.pop())
        return "".join(result)