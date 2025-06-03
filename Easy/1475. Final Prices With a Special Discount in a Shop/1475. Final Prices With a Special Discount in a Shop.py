class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                prices[j] -= prices[i]
            stack.append(i)
        return prices