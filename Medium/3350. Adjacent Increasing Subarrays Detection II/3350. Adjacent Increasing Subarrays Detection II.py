class Solution(object):
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
        
        # 1. Ön Hesaplama: increase_len[i], nums[i] ile başlayan
        #    en uzun kesinlikle artan alt dizinin uzunluğudur.
        increase_len = [0] * N
        increase_len[N - 1] = 1
        
        for i in range(N - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                # Kendisi + bir sonraki elemanla başlayan artan dizinin uzunluğu
                increase_len[i] = 1 + increase_len[i + 1]
            else:
                increase_len[i] = 1 # Sadece kendi başına 1 uzunluğunda
        
        # 2. Kontrol Fonksiyonu: Belirli bir k için iki bitişik
        #    kesinlikle artan alt dizi olup olmadığını kontrol eder.
        def can_find(k):
            if k == 0:
                return True
            
            # En az 2k eleman olmalı
            if 2 * k > N:
                return False
            
            # Alt dizi başlangıç indeksi a için olası aralık: [0, N - 2k]
            # a: ilk alt dizinin başlangıcı
            # a+k: ikinci alt dizinin başlangıcı
            for a in range(N - 2 * k + 1):
                # Birinci alt dizi: nums[a...a+k-1]
                # İkinci alt dizi: nums[a+k...a+2k-1]
                
                # increase_len[a] >= k: nums[a] ile başlayan artan dizi en az k uzunluğunda mı?
                is_first_increasing = increase_len[a] >= k
                
                # increase_len[a+k] >= k: nums[a+k] ile başlayan artan dizi en az k uzunluğunda mı?
                is_second_increasing = increase_len[a + k] >= k
                
                if is_first_increasing and is_second_increasing:
                    return True
            
            return False

        # 3. İkili Arama: Maksimum k'yı bulma
        
        # k'nın olası aralığı: [0, N // 2]
        low = 0
        high = N // 2
        max_k = 0
        
        while low <= high:
            # mid = (low + high + 1) // 2 : Sağ ağırlıklı orta (sonucu artırmaya meyilli)
            mid = low + (high - low) // 2
            
            if can_find(mid):
                # mid uzunluğu mümkün. Daha büyük bir k deneyelim.
                max_k = mid
                low = mid + 1
            else:
                # mid uzunluğu çok büyük. Daha küçük bir k deneyelim.
                high = mid - 1
                
        return max_k