class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # arr dizisini yerinde (in-place) sıralıyoruz.
        # Sıralama kriteri olarak bir tuple veriyoruz: 
        # 1. Eleman: Sayının ikili gösterimindeki '1'lerin sayısı
        # 2. Eleman: Sayının kendi değeri (eşitlik durumunda tie-breaker olarak kullanılır)
        arr.sort(key=lambda x: (bin(x).count('1'), x))
        
        return arr

        # Not: Python 3.10 ve üzeri sürümlerde bin(x).count('1') yerine 
        # doğrudan x.bit_count() kullanılarak daha performanslı bir çözüm de yazılabilir:
        # arr.sort(key=lambda x: (x.bit_count(), x))
        # return arr