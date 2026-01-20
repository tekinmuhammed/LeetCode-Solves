class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            if x == 2:
                ans.append(-1)
            else:
                # Mantık: x asal sayı olduğu için tektir (2 hariç).
                # x'in binary gösterimi ...011...1 şeklindedir (sonda en az bir tane 1 var).
                # Biz x'i elde etmek için, x'in sondaki 1 bloğunun en büyük basamağındaki
                # 1'i 0 yapan sayıyı bulmalıyız.
                
                # 1. Adım: x + 1 yaparak sondaki 1 bloğunu 0'a, hemen solundaki 0'ı 1'e çevir.
                # Örnek: 11 (1011) -> 12 (1100)
                next_val = x + 1
                
                # 2. Adım: next_val içindeki en sağdaki 1 bitini bul (Lowbit).
                # Bu bitin değeri, bizim çıkarmamız gereken değerin 2 katıdır.
                # Örnek: 12 (1100) -> lowbit 4 (100)
                lowbit = next_val & -next_val
                
                # 3. Adım: x'ten lowbit'in yarısını çıkar.
                # Örnek: 11 - (4 // 2) = 11 - 2 = 9.
                ans.append(x - (lowbit >> 1))
                
        return ans