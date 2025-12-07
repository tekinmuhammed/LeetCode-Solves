class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        # If both low and high are even → number of odds is (high - low) // 2
        # Otherwise → (high - low) // 2 + 1
        return ((high - low) // 2) + (1 if low % 2 == 1 or high % 2 == 1 else 0)