class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 1        # at least one period (first day)
        length = 1       # current smooth descent length

        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                length += 1
            else:
                length = 1
            total += length

        return total