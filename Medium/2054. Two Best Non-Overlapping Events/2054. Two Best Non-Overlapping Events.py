from bisect import bisect_right

class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort(key=lambda x: x[1])
        max_value = 0
        max_values= []
        end_times = []
        for _, end, value in events:
            max_value = max(max_value, value)
            max_values.append(max_value)
            end_times.append(end)
        result = 0
        for start, _, value in events:
            idx = bisect_right(end_times, start - 1) - 1
            if idx >= 0:
                result = max(result, value + max_values[idx])
            else:
                result = max(result, value)
        return result