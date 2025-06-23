class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_valid(num):
            def can_partition(s, target, index):
                if index == len(s):
                    return target == 0
                value = 0
                for i in range(index, len(s)):
                    value = value * 10 + int(s[i])
                    if value > target:
                        break
                    if can_partition(s, target - value, i + 1):
                        return True
                return False
            square_str = str(num * num)
            return can_partition(square_str, num, 0)
        total = 0
        for i in range(1, n + 1):
            if is_valid(i):
                total += i * i
        return total