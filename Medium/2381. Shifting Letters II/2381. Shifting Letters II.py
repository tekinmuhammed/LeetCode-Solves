class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        s = list(s)
        delta = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            if direction == 1:
                delta[start] += 1
                delta[end + 1] -= 1
            else:
                delta[start] -= 1
                delta[end + 1] += 1
        for i in range(1, len(delta)):
            delta[i] += delta[i - 1]
        for i in range(len(s)):
            shift = delta[i] % 26
            s[i] = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        return "".join(s)