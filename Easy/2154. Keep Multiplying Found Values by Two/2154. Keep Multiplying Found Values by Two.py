class Solution(object):
    def findFinalValue(self, nums, original):
        s = set(nums)   # O(1) arama için
        
        while original in s:
            original *= 2
            
        return original