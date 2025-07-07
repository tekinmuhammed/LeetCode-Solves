class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)

        for d in s:
            if d != '9':
                max_val = int(s.replace(d, '9'))
                break
        else:
            max_val = num
        
        for d in s:
            if d != '0':
                min_val = int(s.replace(d, '0'))
                break
        else:
            min_val = num
        return max_val - min_val