class Solution(object):
    def reverseBits(self, n):
        result = 0
        
        for _ in range(32):
            result <<= 1        # sola kaydır
            result |= (n & 1)   # son biti ekle
            n >>= 1             # n'i sağa kaydır
        
        return result