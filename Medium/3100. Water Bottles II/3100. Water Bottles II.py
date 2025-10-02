class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            empty -= numExchange
            total += 1
            empty += 1
            numExchange += 1
        
        return total