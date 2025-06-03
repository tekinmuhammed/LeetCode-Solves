from  collections import Counter

class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        freq = Counter(s)
        sorted_chars = sorted(freq.keys(), reverse=True)

        result = []
        while sorted_chars:
            current_char = sorted_chars[0]
            count_to_add = min(freq[current_char], repeatLimit)
            result.append(current_char * count_to_add)
            freq[current_char] -= count_to_add
            if freq[current_char] == 0:
                sorted_chars.pop(0)
            else:
                if len(sorted_chars) == 1:
                    break
                next_char = sorted_chars[1]
                result.append(next_char)
                freq[next_char] -= 1
                if freq[next_char] == 0:
                    sorted_chars.pop(1)
        return ''.join(result)