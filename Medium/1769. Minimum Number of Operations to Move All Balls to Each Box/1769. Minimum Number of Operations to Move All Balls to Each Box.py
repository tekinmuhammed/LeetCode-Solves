class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        a = len(boxes)
        answer = [0] * a

        moves = 0
        count = 0
        for i in range(a):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        moves = 0
        count = 0
        for i in range(a - 1, -1, -1):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count
        return answer