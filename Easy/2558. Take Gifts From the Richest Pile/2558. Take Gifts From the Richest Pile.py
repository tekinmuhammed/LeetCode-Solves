import math

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for _ in range(k):
            max_index = gifts.index(max(gifts))
            gifts[max_index] = int(math.floor(math.sqrt(gifts[max_index])))
        return sum(gifts)
