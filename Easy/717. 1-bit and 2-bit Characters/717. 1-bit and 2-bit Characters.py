class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)

        while i < n - 1:  # last bit is checked separately
            if bits[i] == 1:
                i += 2   # 2-bit character
            else:
                i += 1   # 1-bit character

        return i == n - 1