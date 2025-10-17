import functools

class Solution:
    """
    3003. Maximize the Number of Partitions After Operations
    
    Verilen string s ve tamsayı k için, en fazla bir indeksi değiştirme hakkı kullanarak, 
    string'i her bir bölüm en fazla k farklı karakter içerecek şekilde maksimum sayıda 
    bölmeye ayırmayı hedefler.
    """
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        # Memoization için lru_cache kullanıyoruz.
        # Durum: (mevcut index i, değişiklik yapma hakkı kaldı mı can_change, mevcut bölümün karakter maskesi mask)
        @functools.lru_cache(None)
        def dp(i: int, can_change: bool, mask: int) -> int:
            """
            s[i..n) alt dizesini bölerek elde edilebilecek maksimum bölüm sayısını döndürür.
            
            :param i: Şu anki index.
            :param can_change: True ise henüz değişiklik yapılmamıştır.
            :param mask: Mevcut bölümdeki benzersiz karakterlerin bit maskesi.
            :return: s[i..n) için maksimum bölüm sayısı.
            """
            if i == n:
                # String tamamen bölündü, yeni bir bölüm daha gelmiyor.
                # Ancak problem tanımındaki partition işlemi prefix'i silip 1 bölüm ekler, 
                # bu da boş string için 0 anlamına gelir. 
                return 0

            # Mevcut karaktere karşılık gelen bit.
            bit_cur_char = 1 << (ord(s[i]) - ord('a'))

            # --- A: Karakteri DEĞİŞTİRMEDEN deneme ---

            # Yeni maskeyi hesapla
            new_mask = mask | bit_cur_char
            
            res = 0
            
            if new_mask.bit_count() > k:
                # Mevcut karakteri eklemek k'yi aşıyor. Yeni bir bölüm başlatmalıyız.
                # 1. Bölüm sayısı artar (+1).
                # 2. Yeni bölüm şimdiki karakterden başlar, maskesi 'bit_cur_char' olur.
                # 3. Değişiklik hakkı korunur (can_change).
                res = 1 + dp(i + 1, can_change, bit_cur_char)
            else:
                # Mevcut karakter mevcut bölüme eklenebilir.
                # 1. Bölüm sayısı artmaz.
                # 2. Yeni maske 'new_mask' olur.
                # 3. Değişiklik hakkı korunur (can_change).
                res = dp(i + 1, can_change, new_mask)

            # --- B: Karakteri DEĞİŞTİREREK deneme (sadece can_change True ise) ---
            if can_change:
                # Karakteri değiştirmeyi denersek, bir sonraki çağrıda can_change False olacak.
                for j in range(26):  # 26 olası yeni karakteri (a'dan z'ye) dener
                    bit_brute_char = 1 << j

                    # Yeni maskeyi hesapla
                    new_mask_changed = mask | bit_brute_char

                    if new_mask_changed.bit_count() > k:
                        # Değiştirilmiş karakteri eklemek k'yi aşıyor. Yeni bir bölüm başlatmalıyız.
                        # 1. Bölüm sayısı artar (+1).
                        # 2. Yeni bölüm şimdiki (değiştirilmiş) karakterden başlar, maskesi 'bit_brute_char' olur.
                        # 3. Değişiklik hakkı kullanılır (False).
                        res = max(res, 1 + dp(i + 1, False, bit_brute_char))
                    else:
                        # Değiştirilmiş karakter mevcut bölüme eklenebilir.
                        # 1. Bölüm sayısı artmaz.
                        # 2. Yeni maske 'new_mask_changed' olur.
                        # 3. Değişiklik hakkı kullanılır (False).
                        res = max(res, dp(i + 1, False, new_mask_changed))

            return res

        # İlk bölüm, tüm stringin bir bölümü olarak sayılacağı için, 
        # fonksiyonun döndürdüğü bölme işlemlerine +1 eklememiz gerekir.
        # Başlangıçta index 0, değişiklik hakkı var (True), maske 0 (boş bölüm).
        return dp(0, True, 0) + 1