class Solution(object):
    def intersectionSizeTwo(self, intervals):
        # Sort by end asc, and start desc
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        res = 0
        # last two chosen points
        a = -1
        b = -1
        
        for start, end in intervals:
            # Case 1: both points are outside the interval
            if start > b:
                # we need 2 new numbers
                res += 2
                b = end
                a = end - 1
            # Case 2: only one point is inside
            elif start > a:
                # need 1 more number
                res += 1
                a = b
                b = end
        
        return res