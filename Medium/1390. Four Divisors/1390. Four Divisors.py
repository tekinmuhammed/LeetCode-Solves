import math

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        total_sum = 0
        
        for num in nums:
            # Bölen sayısını ve toplamını tutacak değişkenler
            count = 0
            div_sum = 0
            
            # 1'den sayının kareköküne kadar (karekök dahil) kontrol et
            limit = int(math.sqrt(num))
            
            for i in range(1, limit + 1):
                if num % i == 0:
                    # i bir bölendir.
                    # Eğer i tam karekök ise (örn: num=4, i=2), sadece 1 bölen sayılır.
                    if i * i == num:
                        count += 1
                        div_sum += i
                    else:
                        # Değilse, hem i hem de num/i bölendir.
                        # Örn: num=21, i=3 ise, bölenler 3 ve 7'dir.
                        count += 2
                        div_sum += (i + (num // i))
                    
                    # Optimizasyon: Eğer bölen sayısı 4'ü geçerse, daha fazla saymaya gerek yok.
                    if count > 4:
                        break
            
            # Eğer tam olarak 4 böleni varsa, toplamı genel sonuca ekle
            if count == 4:
                total_sum += div_sum
                
        return total_sum