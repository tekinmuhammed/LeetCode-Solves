class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)

        # Initial profit without modification
        base_profit = 0
        for i in range(n):
            base_profit += strategy[i] * prices[i]

        # If we apply modification on a window [l, r]
        # First k//2 -> 0 (hold)
        # Last k//2  -> 1 (sell)
        half = k // 2

        # Build delta array: how much profit changes if strategy[i] is changed
        # to hold (0) or sell (1)
        to_hold = [-(strategy[i] * prices[i]) for i in range(n)]
        to_sell = [(1 - strategy[i]) * prices[i] for i in range(n)]

        # Prefix sums
        prefix_hold = [0]
        prefix_sell = [0]
        for i in range(n):
            prefix_hold.append(prefix_hold[-1] + to_hold[i])
            prefix_sell.append(prefix_sell[-1] + to_sell[i])

        max_gain = 0

        # Sliding window of size k
        for l in range(0, n - k + 1):
            mid = l + half
            r = l + k

            gain_hold = prefix_hold[mid] - prefix_hold[l]
            gain_sell = prefix_sell[r] - prefix_sell[mid]

            max_gain = max(max_gain, gain_hold + gain_sell)

        return base_profit + max_gain