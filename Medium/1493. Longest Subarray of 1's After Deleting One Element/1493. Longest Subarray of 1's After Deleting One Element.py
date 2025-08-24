class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # Eğer 0 sayısı 1’den fazlaysa sol pointer kaydır
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # (right - left) çünkü bir eleman silmek zorundayız
            max_len = max(max_len, right - left)

        return max_len