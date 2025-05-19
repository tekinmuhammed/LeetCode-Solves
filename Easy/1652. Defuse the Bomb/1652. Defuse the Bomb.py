class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        if k == 0:
            return [0] * n
        result = [0] * n
        if k > 0:
            for i in range(n):
                result[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
        else:
            for i in range(n):
                result[i] = sum(code[(i + j) % n] for j in range(k, 0))
        return result