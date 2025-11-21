class Solution(object):
    def kthCharacter(self, k):
        word = "a"
        
        while len(word) < k:
            # Her karakteri bir sonraki harfe çevir
            new_part = ''.join(chr(ord(c) + 1) for c in word)
            # Yeni stringi ekle
            word += new_part
        
        return word[k - 1]