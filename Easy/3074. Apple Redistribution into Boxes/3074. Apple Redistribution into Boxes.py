class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)

        capacity.sort(reverse=True)

        curr = 0
        count = 0

        for cap in capacity:
            curr += cap
            count += 1
            if curr >= total_apples:
                return count