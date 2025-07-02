class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()
        
        def can_form_pairs(threshold):
            count = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= threshold:
                    count += 1
                    i += 2  # skip both used elements
                else:
                    i += 1
            return count >= p
        
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                right = mid
            else:
                left = mid + 1
        
        return left