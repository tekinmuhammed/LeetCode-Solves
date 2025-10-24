class Solution:
    """
    Verilen n tam sayısından kesinlikle büyük olan en küçük sayısal olarak 
    dengeli sayıyı (Next Greater Numerically Balanced Number) bulur.
    
    Sayısal olarak dengeli sayı: Her d rakamı, sayıda tam olarak d kez geçer.
    """
    
    def isBalance(self, num: int) -> bool:
        """
        Bir sayının sayısal olarak dengeli olup olmadığını kontrol eder.
        
        :param num: Kontrol edilecek tam sayı.
        :return: Sayı dengeliyse True, aksi takdirde False.
        """
        # Her bir rakamın (0'dan 9'a) sayımını tutar.
        # Maksimum rakam 6 olabilir (666666 en büyük 10^6'dan küçük/yakın dengeli sayı).
        count = [0] * 10
        temp_num = num
        
        while temp_num > 0:
            digit = temp_num % 10
            
            # 0 rakamının sayısal olarak dengeli bir sayıda bulunmaması gerekir, 
            # çünkü 0'ın 0 kez geçmesi gerekir. Eğer 0 geçerse dengeli olamaz.
            if digit == 0:
                return False
            
            count[digit] += 1
            temp_num //= 10
            
        # 1'den 9'a kadar olan her rakamın sayımını kontrol et.
        for d in range(1, 10):
            # 1. Eğer rakam (d) sayıda geçtiyse (count[d] > 0), 
            # 2. Sayımının tam olarak rakamın kendisine (d) eşit olması gerekir.
            if count[d] > 0 and count[d] != d:
                return False
                
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        """
        n'den büyük olan en küçük sayısal olarak dengeli sayıyı döndürür.
        """
        # n'den kesinlikle büyük olması gerektiği için n+1'den başla.
        current_num = n + 1
        
        # Sayısal olarak dengeli bir sayı bulana kadar tek tek artır ve kontrol et.
        # Maksimum n kısıtı 10^6 olduğundan, sonraki en küçük dengeli sayı da 
        # makul bir aralıkta olacaktır (en fazla 1333333).
        while True:
            if self.isBalance(current_num):
                return current_num
            current_num += 1