class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        carry = 0
        
        # Stringi sağdan sola doğru, en baştaki (0. indeks) bit hariç tara.
        # Çünkü sayıyı 1'e düşürmeye çalışıyoruz.
        for i in range(len(s) - 1, 0, -1):
            
            # Mevcut bit ile eldeki (carry) değeri topla
            current_bit = int(s[i]) + carry
            
            if current_bit == 1:
                # Toplam 1 ise sayı tektir.
                # 1 ekleme işlemi ve ardından gelen 2'ye bölme işlemi için toplam 2 adım.
                # 1 eklediğimiz için sonraki basamağa aktarılacak carry 1 olur.
                steps += 2
                carry = 1
            else:
                # Toplam 0 veya 2 ise sayı çifttir.
                # Sadece 2'ye bölme işlemi yapılır (1 adım).
                # carry 2 ise (1+carry), elde 1 olmaya devam eder. 0 ise 0 kalır.
                steps += 1
                
        # Döngü bittiğinde en sol baştaki 1'deyiz (s[0] her zaman 1'dir).
        # Eğer elde kalan bir carry varsa (yani en baştaki 1, 1+1'den 10'a dönüştüyse), 
        # onu da 2'ye bölmek için 1 adım daha gerekir.
        return steps + carry