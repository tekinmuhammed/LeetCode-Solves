class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ball_colors = {}
        color_frequency = {}
        distinct_colors_count = 0
        result = []
        for x, y in queries:
            if x in ball_colors:
                old_color = ball_colors[x]
                color_frequency[old_color] -= 1
                if color_frequency[old_color] == 0:
                    distinct_colors_count -= 1
            ball_colors[x] = y
            if y not in color_frequency:
                color_frequency[y] = 0
            color_frequency[y] += 1
            if color_frequency[y] == 1:
                distinct_colors_count += 1
            result.append(distinct_colors_count)
        return result