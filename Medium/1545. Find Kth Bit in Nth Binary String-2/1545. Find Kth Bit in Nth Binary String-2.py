class Solution(object):
    def findKthBit(self, n, k):
        def helper(n, k):
            if n == 1:
                return '0'
            
            mid = 1 << (n - 1)   # 2^(n-1)
            
            if k == mid:
                return '1'
            elif k < mid:
                return helper(n - 1, k)
            else:
                # symmetric position
                mirrored = mid - (k - mid)
                bit = helper(n - 1, mirrored)
                # invert
                return '1' if bit == '0' else '0'
        
        return helper(n, k)