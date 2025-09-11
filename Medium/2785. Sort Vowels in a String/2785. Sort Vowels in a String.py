class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set("aeiouAEIOU")

        # 1. Seslileri topla
        vowel_list = [ch for ch in s if ch in vowels]

        # 2. ASCII değerlerine göre sırala
        vowel_list.sort()

        # 3. Yeni stringi oluştur
        result = []
        idx = 0
        for ch in s:
            if ch in vowels:
                result.append(vowel_list[idx])
                idx += 1
            else:
                result.append(ch)

        return "".join(result)