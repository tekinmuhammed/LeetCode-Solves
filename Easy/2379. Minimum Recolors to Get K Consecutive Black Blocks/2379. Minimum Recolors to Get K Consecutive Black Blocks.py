class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_recolor = blocks[:k].count('W')
        current_recolor = min_recolor
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_recolor -= 1
            if blocks[i] == 'W':
                current_recolor += 1
            min_recolor = min(min_recolor, current_recolor)
        return min_recolor