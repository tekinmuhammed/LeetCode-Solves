class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')
        result = []

        # Minimum farkı bul
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            min_diff = min(min_diff, diff)

        # Minimum farka sahip çiftleri topla
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                result.append([arr[i], arr[i + 1]])

        return result