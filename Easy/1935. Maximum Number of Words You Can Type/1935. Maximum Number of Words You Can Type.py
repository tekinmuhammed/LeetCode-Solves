class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)   # Bozuk tuşları kümeye alıyoruz
        words = text.split()          # Metni kelimelere ayırıyoruz
        
        count = 0
        for word in words:
            if not any(ch in broken for ch in word):  # Eğer kelimede bozuk harf yoksa
                count += 1
        return count