class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        """
        nums dizisindeki tüm elemanları sıfıra eşitleyen geçerli başlangıç (curr) 
        ve hareket yönü kombinasyonlarının sayısını döndürür.
        """
        n = len(nums)
        valid_selections = 0
        
        # Suffix Sum (Arka Toplam): SuffixSum[i], nums[i+1]'den nums[n-1]'e kadar olan elemanların toplamıdır.
        # Bu, sağ kısımdaki toplamı temsil eder.
        total_sum = sum(nums)
        suffix_sum = total_sum
        
        # Prefix Sum (Ön Toplam): PrefixSum[i], nums[0]'dan nums[i-1]'e kadar olan elemanların toplamıdır.
        # Bu, sol kısımdaki toplamı temsil eder.
        prefix_sum = 0
        
        for i in range(n):
            # i, curr pozisyonunu temsil eder.
            
            # Güncel nums[i] elemanını suffix_sum'dan çıkarıyoruz, çünkü i'nin sağındaki toplamı hesaplıyoruz.
            suffix_sum -= nums[i] 
            
            # Başlangıç pozisyonu (curr) yalnızca nums[i] == 0 olan yerler olabilir.
            if nums[i] == 0:
                # Geçerli bir seçim için, i'nin solundaki toplam (prefix_sum) ile 
                # i'nin sağındaki toplam (suffix_sum) arasındaki farkın en fazla 1 olması gerekir.
                # abs(PrefixSum[i-1] - SuffixSum[i+1]) <= 1
                
                diff = abs(prefix_sum - suffix_sum)
                
                if diff <= 1:
                    if diff == 0:
                        # Sol ve sağ toplamlar eşit: Her iki yöne (sola veya sağa) gitmek geçerlidir.
                        valid_selections += 2
                    elif diff == 1:
                        # Sol ve sağ toplamlar arasında 1 fark var: Yalnızca daha büyük toplama sahip 
                        # olan tarafa doğru ilk adımı atmak geçerlidir. (1 geçerli seçim)
                        valid_selections += 1
            
            # Güncel nums[i] elemanını prefix_sum'a ekliyoruz, bir sonraki döngü adımında i'nin solundaki toplamı hesaplayacağız.
            prefix_sum += nums[i]

        return valid_selections

# Örnek 1: nums = [1, 0, 2, 0, 3]
# solution = Solution()
# print(solution.countValidSelections([1, 0, 2, 0, 3])) # Çıktı: 2

# Örnek 2: nums = [2, 3, 4, 0, 4, 1, 0]
# solution = Solution()
# print(solution.countValidSelections([2, 3, 4, 0, 4, 1, 0])) # Çıktı: 0