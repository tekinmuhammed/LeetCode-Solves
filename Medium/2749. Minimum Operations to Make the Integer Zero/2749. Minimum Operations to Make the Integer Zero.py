class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        for k in range(1, 61):  # en fazla 60 adım çünkü 2^i ≤ 2^60
            target = num1 - k * num2
            if target < 0:
                return -1
            # target ikilikte yazılabilir ve en az k bit gerekir
            if bin(target).count("1") <= k <= target:
                return k
        return -1