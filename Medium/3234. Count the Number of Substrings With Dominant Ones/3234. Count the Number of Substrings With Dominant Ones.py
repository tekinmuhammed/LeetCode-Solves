import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        
        # Sınır değerini belirleme (B = floor(sqrt(n)) + 1 veya ~317)
        # N0 > B ise, N0^2 > 100000 olur ki, bu da N1 <= N (max 10^5) ile mümkün değildir.
        # Bu nedenle, sadece N0 <= B durumlarını kontrol etmemiz yeterli.
        B = int(math.sqrt(n)) + 1
        
        # P[k]: dizedeki k. sıfırın indeksi (1-tabanlı)
        # P[0] = -1 olarak tanımlayalım (dizenin öncesi)
        zero_indices = [-1]
        for i, char in enumerate(s):
            if char == '0':
                zero_indices.append(i)
        
        total_count = 0
        
        # 1. Durum: N0 = 0 (Alt dizide hiç sıfır yoksa)
        # Sadece '1'lerden oluşan tüm alt dizeler baskındır.
        # N0=0 -> N1 >= 0^2 -> N1 >= 0 (Her zaman doğru)
        # Tüm '1' gruplarının alt dizelerini say.
        
        count_ones = 0
        for char in s:
            if char == '1':
                count_ones += 1
            else:
                # '1' grubundaki alt dize sayısı: count_ones * (count_ones + 1) / 2
                total_count += count_ones * (count_ones + 1) // 2
                count_ones = 0
        # Son '1' grubunu ekle
        total_count += count_ones * (count_ones + 1) // 2


        # 2. Durum: 1 <= N0 <= B
        # zero_indices[k]: k. sıfırın indeksi (k=1'den başlar)
        # Alt dize sıfırları zero_indices[i] ve zero_indices[j] arasında olan alt dizeleri sayarız
        
        # i: Alt dizedeki ilk sıfırın sırası (1'den başlar)
        for i in range(1, len(zero_indices)):
            # j: Alt dizedeki son sıfırın sırası
            # Alt dizideki sıfır sayısı k = j - i + 1
            for j in range(i, min(len(zero_indices), i + B)):
                # k = j - i + 1: Alt dizideki sıfır sayısı (N0)
                k = j - i + 1
                
                # N0^2
                k_squared = k * k
                
                # p_start: İlk sıfırın indeksi (i. sıfır)
                # p_end: Son sıfırın indeksi (j. sıfır)
                p_start = zero_indices[i]
                p_end = zero_indices[j]
                
                # Bu alt dizedeki (p_start'tan p_end'e) birlerin sayısı:
                # N1_core = (p_end - p_start + 1) - k
                
                # Bu alt dizenin uzunluğu (min_len): p_end - p_start + 1
                # Birlerin sayısı (N1) >= N0^2 koşulu:
                # (Alt dize Uzunluğu) - N0 >= N0^2
                # Alt dize Uzunluğu >= N0 + N0^2

                # Alt dizenin başlangıç indeksi: p_start - L_prefix
                # Alt dizenin bitiş indeksi: p_end + L_suffix
                
                # Alt dizenin sıfırları p_start'tan p_end'e kadar olan 
                # kısmın uzunluğu: L_core = p_end - p_start + 1
                # N1_core = L_core - k 
                
                # Minimum uzunluk koşulunu hesapla:
                # L_min = p_end - p_start + k_squared + k
                
                # Alt dize (i. sıfır dahil, j. sıfır hariç)
                # Başlangıç konumu: zero_indices[i-1] + 1
                # Bitiş konumu: zero_indices[j]
                
                # Alt dizenin başlangıcı (start_index):
                # i. sıfırdan önceki '1' grubu içinden bir yer (zero_indices[i-1] + 1'den p_start'a kadar)
                start_boundary = zero_indices[i-1] + 1
                
                # Alt dizenin bitişi (end_index):
                # j. sıfırdan sonraki '1' grubu içinden bir yer (p_end'den zero_indices[j+1] - 1'e kadar)
                # zero_indices[j+1]: eğer j son sıfır değilse, bir sonraki sıfırın indeksi
                # Eğer j en sondaki sıfır ise, n olur
                end_boundary = n
                if j + 1 < len(zero_indices):
                    end_boundary = zero_indices[j+1]
                end_boundary -= 1 # 1'lerin bittiği yer
                
                
                # Alt dizenin başlangıcı: i. sıfırın bulunduğu p_start
                # Alt dizenin bitişi: j. sıfırın bulunduğu p_end
                
                # Aradaki '1' sayısı (i. sıfırdan önceki ve j. sıfırdan sonraki 1'ler hariç):
                # N1_core = (p_end - p_start + 1) - k
                N1_core = p_end - p_start + 1 - k
                
                # Koşulun sağlanması için fazladan gereken '1' sayısı:
                # N1_gerekli = N0^2 - N1_core
                N1_gerekli = k_squared - N1_core
                
                # Eğer N1_gerekli zaten 0 veya negatif ise, çekirdek alt dize [p_start, p_end]
                # bile koşulu sağlıyor demektir.
                if N1_gerekli <= 0:
                    N1_gerekli = 0
                
                # Başlangıçtan (i. sıfırdan önce) çekebileceğimiz maksimum '1' sayısı:
                # p_start - (zero_indices[i-1] + 1)
                max_prefix_ones = p_start - start_boundary
                
                # Bitişten (j. sıfırdan sonra) çekebileceğimiz maksimum '1' sayısı:
                # end_boundary - p_end
                max_suffix_ones = end_boundary - p_end
                
                
                # Alt dizenin başlangıcı ve bitişi için gereken fazladan '1' sayısı (prefix_ones + suffix_ones)
                # toplamı N1_gerekli'den büyük veya eşit olmalıdır.
                # prefix_ones + suffix_ones >= N1_gerekli
                
                # Minimum prefix_ones + suffix_ones toplamı N1_gerekli'dir.
                # Maksimum toplam ise max_prefix_ones + max_suffix_ones'tır.
                
                # Alt dize sayısını bulmak için, prefix_ones ve suffix_ones'ın olası kombinasyonlarını sayarız:
                # 0 <= prefix_ones <= max_prefix_ones
                # 0 <= suffix_ones <= max_suffix_ones
                # prefix_ones + suffix_ones >= N1_gerekli
                
                
                # L_prefix: prefix '1' sayısı
                # L_suffix: suffix '1' sayısı
                
                # L_prefix'in alabileceği en küçük değer: max(0, N1_gerekli - max_suffix_ones)
                L_prefix_min = max(0, N1_gerekli - max_suffix_ones)
                
                # L_prefix'in alabileceği en büyük değer: min(max_prefix_ones, N1_gerekli)
                L_prefix_max = min(max_prefix_ones, N1_gerekli)
                
                # Eğer L_prefix_min > max_prefix_ones (yani prefix + suffix yetersiz) 
                # veya N1_gerekli > max_prefix_ones + max_suffix_ones ise, bu alt dizeyi oluşturamayız.
                if N1_gerekli > max_prefix_ones + max_suffix_ones:
                    continue # Alt dize oluşturmak imkansız
                
                
                # L_prefix'in alabileceği toplam değer aralığı: [L_prefix_min, max_prefix_ones]
                # Bu aralıkta koşul sağlandığı gibi,
                # L_prefix > N1_gerekli durumlarında da sağlanır.
                
                # L_prefix'in alabileceği değerler:
                # [L_prefix_min, max_prefix_ones] aralığındaki her L_prefix için
                # L_suffix'in alabileceği değerler:
                # [max(0, N1_gerekli - L_prefix), max_suffix_ones]
                
                # Toplam sayıyı basitleştirilmiş bir şekilde hesaplayalım:
                # Toplam alt dize sayısı = (max_prefix_ones - L_prefix_min + 1) * (max_suffix_ones + 1)
                #   - (kalan alt dizi sayısı)
                
                # En basit yol:
                # Toplam alt dize sayısı:
                # Toplam olası kombinasyon sayısı: (max_prefix_ones + 1) * (max_suffix_ones + 1)
                #   - Koşulu sağlamayanların sayısı (N1_prefix + N1_suffix < N1_gerekli)
                
                
                # L_prefix [0, max_prefix_ones]
                # L_suffix [0, max_suffix_ones]
                
                # N1_gerekli > 0 ise, koşulu sağlamayanların sayısı:
                # L_prefix + L_suffix = N1_gerekli - 1
                # N1_gerekli - 2, ..., 0
                
                # Koşulu sağlayan kombinasyon sayısı (L_prefix + L_suffix >= N1_gerekli):
                # L_prefix, [L_prefix_min, max_prefix_ones] aralığında
                
                current_sub_count = 0
                for L_prefix in range(L_prefix_min, max_prefix_ones + 1):
                    # L_prefix sabit iken, L_suffix için alt sınır:
                    L_suffix_min = max(0, N1_gerekli - L_prefix)
                    
                    # L_suffix'in alabileceği değer aralığı: [L_suffix_min, max_suffix_ones]
                    
                    # L_suffix_min <= max_suffix_ones olmalıdır. 
                    # Bu kontrol zaten N1_gerekli > max_prefix_ones + max_suffix_ones kontrolüyle yapıldı.
                    
                    # L_suffix'in alabileceği değer sayısı: max_suffix_ones - L_suffix_min + 1
                    current_sub_count += (max_suffix_ones - L_suffix_min + 1)
                    
                total_count += current_sub_count

        return total_count