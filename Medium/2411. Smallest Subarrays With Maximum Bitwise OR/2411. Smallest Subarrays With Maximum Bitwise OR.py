class Solution(object):
    def smallestSubarrays(self, nums):
        n = len(nums)
        last = [0] * 32  # Her bit için son görülme yeri
        res = [1] * n    # Varsayılan olarak her eleman kendi başına yeterli olabilir

        for i in range(n - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    last[j] = i  # Bu bit burada görüldü

            # En uzak bit'e kadar gitmemiz gereken index'i bul
            max_last = i
            for j in range(32):
                if last[j] > max_last:
                    max_last = last[j]

            res[i] = max_last - i + 1

        return res