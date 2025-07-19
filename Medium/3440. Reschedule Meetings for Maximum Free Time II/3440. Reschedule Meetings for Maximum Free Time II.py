class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        t1 = 0
        t2 = 0
        res = 0

        for i in range(n):
            left1 = 0 if i == 0 else endTime[i-1]
            right1 = eventTime if i == n-1 else startTime[i+1]

            if endTime[i] - startTime[i] <= t1:
                res = max(res, right1 - left1)
            else:
                res = max(res, right1 - left1 - (endTime[i] - startTime[i]))
            t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i-1]))
            
            left2 = 0 if i == n-1 else endTime[n-i-2]
            right2 = eventTime if i == 0 else startTime[n-i]

            if endTime[n-i-1] - startTime[n-i-1] <= t2:
                res = max(res, right2 - left2)
            else:
                res = max(res, right2 - left2 - (endTime[n-i-1] - startTime[n-i-1]))
            t2 = max(t2, (eventTime if i==0 else startTime[n-i]) - endTime[n-i-1])

        return res