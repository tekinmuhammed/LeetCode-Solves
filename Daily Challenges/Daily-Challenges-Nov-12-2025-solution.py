# 🧩 LeetCode 2654 – Minimum Number of Operations to Make All Array Elements Equal to 1

# **Problem Link:** [LeetCode 2654](https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description/)  
# **Difficulty:** Medium

# 🧠 Problem Description 
# [Github LeetCode 2654 – Minimum Number of Operations to Make All Array Elements Equal to 1](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2654.%20Minimum%20Number%20of%20Operations%20to%20Make%20All%20Array%20Elements%20Equal%20to%201)

import math

class Solution:
    """
    2654. Tüm Dizi Elemanlarını 1'e Eşitlemek İçin Minimum İşlem Sayısı
    """
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        # 1. Durum: Dizide zaten 1 varsa
        # İşlem: Dizideki tüm 1 olmayan elemanları 1'e dönüştürmek gerekir.
        # Bu, her 1 olmayan eleman için 1 işlem (kendisi ile 1 komşusu arasında gcd alıp,
        # komşuyu 1 yapmak ve sonra bu komşuyu kullanarak kendisini 1 yapmak)
        # veya daha basitçe, zaten var olan bir 1'i kullanarak yanındaki elemanı 1 yapmak
        # ve bu işlemi domino etkisiyle tüm diziye yaymaktır.
        # Toplam işlem sayısı = n - (1'lerin sayısı)
        ones_count = nums.count(1)
        if ones_count > 0:
            return n - ones_count

        # 2. Durum: Dizide 1 yoksa
        # Amaç: İlk 1'i oluşturmak için gereken minimum işlem sayısını bulmak.
        # İlk 1 oluşturulduktan sonra, toplam işlem sayısı:
        # (İlk 1'i oluşturma işlemleri) + (Geri kalan n-1 elemanı 1 yapma işlemleri)

        min_ops_to_make_one = float('inf')

        # Dizideki her alt dizi için gcd hesapla
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, nums[j])
                
                # Eğer alt dizinin gcd'si 1 ise, bu alt diziyi kullanarak
                # bir 1 oluşturulabilir.
                if current_gcd == 1:
                    # Bu alt dizinin uzunluğu: j - i + 1
                    # Bu alt dizideki bir elemanı 1 yapmak için gereken minimum işlem:
                    # (Uzunluk - 1)
                    # Örneğin, [a, b, c] -> 2 işlem: 
                    # 1. gcd(a, b) ile b'yi değiştir (örneğin)
                    # 2. gcd(a, yeni_b) ile c'yi değiştir (bu adım gcd'nin 1 olmasıyla mümkün)
                    # Aslında en kısa yol:
                    # 1. [a, b, c] -> [a, gcd(b, c), c] 
                    # 2. [a, 1, c] -> 1 işlemde 1 oluşturulur.
                    # 3. Ard arda gelen elemanlar arasındaki gcd işlemleri zinciri ile
                    #    uzunluğu 'l' olan bir alt dizide 1 oluşturmak için 'l-1' işlem gerekir.
                    #    Örnek: [a, b, c], gcd(a, b, c) = 1.
                    #    - Op 1: [a, gcd(b, c), c] (1 işlem)
                    #    - Op 2: [gcd(a, gcd(b, c)), gcd(b, c), c] -> [1, 1, c] 
                    #      Eğer gcd(a, gcd(b,c)) = 1 ise. Bu garanti değil.
                    #
                    # Doğru yaklaşım:
                    # Bir uzunluğu 'l' olan alt dizinin gcd'si 1 ise, l-1 işlemle
                    # o alt dizinin **bir** elemanı 1 yapılabilir.
                    # Örneğin, [6, 3, 4], gcd=1. Uzunluk l=3. İşlem: l-1 = 2
                    # 1. [6, gcd(3, 4), 4] = [6, 1, 4] (1 işlem) -> Yanlış.
                    # İşlem sadece komşu elemanlar arasında.
                    # [6, 3, 4]
                    # Op 1: i=1, nums[1] = gcd(3, 4) = 1. -> [6, 1, 4]. (1 işlem)
                    # İlk 1'i oluşturmak için gereken minimum işlem: j - i
                    # Bu, alt dizideki ilk elemandan (nums[i]) başlayıp,
                    # son elemana (nums[j]) doğru ilerleyerek ardışık gcd'ler alıp,
                    # bir elemanı 1 yapmayı sağlar.
                    # Toplam işlem sayısı: j - i
                    
                    ops_to_make_one = j - i
                    min_ops_to_make_one = min(min_ops_to_make_one, ops_to_make_one)
                    
                    # En kısa alt diziyi bulduğumuz için iç döngüden çıkabiliriz.
                    break 

        # 3. Durum: İlk 1 oluşturulamıyorsa
        if min_ops_to_make_one == float('inf'):
            # Eğer tüm dizinin bile gcd'si 1 değilse, imkansızdır.
            # (Zaten min_ops_to_make_one hesaplanırken bu durum da kapsanır:
            # eğer en kısa 1 üreten alt dizi bulunamazsa, inf kalır.)
            return -1

        # 4. Durum: İlk 1 oluşturulabilirse
        # Toplam işlem sayısı = (İlk 1'i oluşturma işlemleri) + (Geri kalan n-1 elemanı 1 yapma işlemleri)
        # Geri kalan n-1 elemanı 1 yapmak için, oluşan 1'i kullanırız.
        # Bu 1'i, yanındaki elemanı 1 yapmak için kullanırız, bu da n-1 işlem gerektirir.
        return min_ops_to_make_one + (n - 1)