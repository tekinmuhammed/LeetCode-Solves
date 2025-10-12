import functools
import math

class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        MOD = 1_000_000_007
        N = len(nums)

        # 1. Kombinasyon ve Modüler Üs Alma Hazırlığı
        
        # Modüler Üs Alma
        def mod_pow(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        # Kombinasyon (Binom Katsayısı) için Pascal Üçgeni veya önceden hesaplama
        # m <= 30 olduğu için basitçe önceden hesaplayabiliriz.
        MAX_M = 30
        comb = [[0] * (MAX_M + 1) for _ in range(MAX_M + 1)]
        for i in range(MAX_M + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        # 2. Dinamik Programlama (DP)
        
        # dp[i][j][carry][k_prime]: nums[i...N-1] arasından j eleman daha seçilerek ve 
        # carry elde ile toplam ayarlanmış bit sayısının k_prime olduğu tüm durumlar için, 
        # kalan j eleman seçimlerinin çarpımlarının toplamı.
        # i: mevcut üs (0'dan N'e kadar)
        # j: kalan seq uzunluğu (0'dan m'ye kadar)
        # carry: i. basamağa gelen elde (0'dan m'ye kadar)
        # k_prime: kalan basamaklardan itibaren gerekli ayarlanmış bit sayısı (0'dan k'ya kadar)

        # N <= 50, m <= 30, k <= 30. Boyut: 51 x 31 x 31 x 31.
        # İlk 3 boyut için lru_cache kullanacağız, k'yi ise doğrudan DP durumuna dahil edeceğiz.

        # DP fonksiyonu
        @functools.lru_cache(None)
        def dp(i: int, j: int, carry: int) -> dict[int, int]:
            """
            i: şu anki üs/nums indeksi (2^i)
            j: seq'de geriye kalan uzunluk
            carry: i. basamağa gelen elde
            Dönüş: {k_prime: toplam_çarpım} şeklinde bir sözlük
            """
            
            # Taban Durumu 1: Tüm elemanlar seçildi (i = N)
            if i == N:
                if j == 0:
                    # Tüm seq elemanları seçildi (j=0).
                    # Gelen elde (carry) tamamen sonuca katkıda bulunur.
                    # Sonuç: carry'nin ayarlanmış bit sayısı.
                    final_set_bits = carry.bit_count()
                    return {final_set_bits: 1} # 1, boş çarpımın (etkisiz elemanın) toplamı
                else:
                    # Tüm üsler tükendi ama seq tam dolmadı.
                    return {}

            # Taban Durumu 2: Kalan uzunluk 0
            # Bu durum, i=N taban durumunda zaten ele alınmıştır (j=0).
            # Eğer i < N iken j = 0 ise, kalan üsler 0 kez seçilmelidir.
            # Dolayısıyla c=0 ile i+1'e tek bir geçiş olur. Bu DP içinde doğal olarak ele alınır.

            results = {} # Kalan ayarlanmış bit sayısına (k_prime) göre sonuçları tutar

            # nums[i]'yi c kez seçme döngüsü
            for c in range(j + 1): # c: nums[i]'yi seçme sayısı
                
                # Geçiş Hesaplamaları
                # c: nums[i] seçilme sayısı
                # j: kalan uzunluk
                # carry: i. basamağa gelen elde
                
                # i. basamaktaki toplam ve elde
                S = c + carry
                bit_val = S % 2      # i. basamaktaki bit değeri
                next_carry = S // 2  # Sonraki basamağa giden elde
                
                # Yeni kalan uzunluk
                j_prime = j - c
                
                # Çarpım katkısı: (j C c) * (nums[i] ^ c)
                # Kombinasyon: Kalan j yerden c tanesini nums[i]'ye atama yolu sayısı
                comb_term = comb[j][c]
                # Üs: Bu c seçimin çarpıma katkısı
                pow_term = mod_pow(nums[i], c)
                
                contribution_mult = (comb_term * pow_term) % MOD
                
                # Rekürsif çağrı
                next_results = dp(i + 1, j_prime, next_carry)
                
                # Sonuçları birleştirme
                for k_prime_next, product_sum_next in next_results.items():
                    # Kalan ayarlanmış bit sayısı: k_prime_next + bit_val
                    k_prime_current = k_prime_next + bit_val
                    
                    # Eğer k_prime_current > k ise, bu yolu kesebiliriz,
                    # ancak k'yi DP durumuna koymadığımız için kesme yapmayız.
                    # Tüm yolları hesaplayıp sonda filtreleyeceğiz.
                    
                    if k_prime_current not in results:
                        results[k_prime_current] = 0
                    
                    # Yeni toplam: (mevcut katkı) * (geri kalanın toplam çarpımı)
                    new_sum = (contribution_mult * product_sum_next) % MOD
                    results[k_prime_current] = (results[k_prime_current] + new_sum) % MOD

            return results

        # 3. Sonuç Hesaplama
        
        # Başlangıç durumu: dp(i=0, j=m, carry=0)
        final_results = dp(0, m, 0)
        
        # Toplam sonuç, k ayarlanmış bit sayısı için olan değerdir.
        return final_results.get(k, 0)