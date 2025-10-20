class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0
        for op in operations:
            if '+' in op:
                X += 1
            else:
                X -= 1
        return X