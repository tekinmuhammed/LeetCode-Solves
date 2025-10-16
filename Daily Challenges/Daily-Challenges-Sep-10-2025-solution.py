# 1733. Minimum Number of People to Teach

# **Difficulty:** Medium  
# **Link:** [LeetCode 1733](https://leetcode.com/problems/minimum-number-of-people-to-teach/)

# 🧠 Problem Description 
# [Github LeetCode 1733. Minimum Number of People to Teach](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1733.%20Minimum%20Number%20of%20People%20to%20Teach)

class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        # Kullanıcı indexlerini 1'den başlatmak için set yapıyoruz
        langs = [set(l) for l in languages]

        # Ortak dili olmayan arkadaş çiftlerini bul
        need_teach = set()
        for u, v in friendships:
            if langs[u - 1].intersection(langs[v - 1]):
                continue
            need_teach.add(u - 1)
            need_teach.add(v - 1)

        # Eğer herkes konuşabiliyorsa
        if not need_teach:
            return 0

        # Seçilecek dil için minimum kişi sayısı hesapla
        ans = float("inf")
        for lang in range(1, n + 1):
            cnt = 0
            for user in need_teach:
                if lang not in langs[user]:
                    cnt += 1
            ans = min(ans, cnt)

        return ans