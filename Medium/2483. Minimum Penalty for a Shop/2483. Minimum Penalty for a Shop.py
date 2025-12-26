class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        n = len(customers)

        # suffix_Y[i] = i'den sona kadar kaç tane 'Y' var
        suffix_Y = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_Y[i] = suffix_Y[i + 1] + (1 if customers[i] == 'Y' else 0)

        min_penalty = float('inf')
        best_hour = 0
        open_N = 0  # açıkken gelen 'N' sayısı

        for j in range(n + 1):
            penalty = open_N + suffix_Y[j]
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j

            if j < n and customers[j] == 'N':
                open_N += 1

        return best_hour