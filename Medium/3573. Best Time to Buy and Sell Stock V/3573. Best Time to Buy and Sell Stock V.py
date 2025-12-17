class Solution:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        n = len(prices)
        # Eğer işlem yapılacak gün sayısı yetersizse veya k 0 ise kâr 0'dır.
        if k == 0 or n < 2:
            return 0
        
        # Günlük fiyat değişimlerini hesapla
        # diff[i], i. gün ile i+1. gün arasındaki farktır.
        diff = [prices[i+1] - prices[i] for i in range(n-1)]
        
        # Çok küçük bir sayı (negatif sonsuz)
        INF = -float('inf')
        
        # DP Dizileri: İndeks 'j' kaçıncı işlemi yaptığımızı gösterir (1'den k'ya kadar)
        
        # free[j]: j işlem tamamlandı, şu an boşta ve işlem yapmaya hazır.
        free = [INF] * (k + 1)
        free[0] = 0  # 0 işlemle 0 kârdayız.
        
        # cool[j]: j işlem tamamlandı, ama işlemi ŞİMDİ kapattık (Gap kuralı).
        # Bir sonraki adımda işlem başlatamaz, sadece free'ye dönüşebilir.
        cool = [INF] * (k + 1)
        
        # hold_n[j]: j. işlemin içindeyiz (Normal/Long pozisyon)
        hold_n = [INF] * (k + 1)
        
        # hold_s[j]: j. işlemin içindeyiz (Short pozisyon)
        hold_s = [INF] * (k + 1)
        
        for v in diff:
            # Bir sonraki durumları hesaplamak için kopyalarını alıyoruz
            new_free = list(free)
            new_cool = list(cool)
            new_hold_n = list(hold_n)
            new_hold_s = list(hold_s)
            
            for j in range(1, k + 1):
                # --- Normal Pozisyon (Long) ---
                # Ya tutmaya devam et (hold_n[j] + v)
                # Ya da yeni başlat (free[j-1] + v). 
                # Not: free[j-1] bekleme süresi bitmiş temiz durumdur.
                new_hold_n[j] = max(hold_n[j] + v, free[j-1] + v)
                
                # --- Short Pozisyon ---
                # Ya tutmaya devam et (hold_s[j] - v) -> Shortta fiyat düşerse (-v pozitiftir) kazanırız.
                # Ya da yeni başlat (free[j-1] - v)
                new_hold_s[j] = max(hold_s[j] - v, free[j-1] - v)
                
                # --- İşlemi Kapatma (Cooling) ---
                # Normal pozisyonu kapat: hold_n[j] + v
                # Short pozisyonu kapat: hold_s[j] - v
                # Veya aynı gün içinde al-sat (Anlık işlem): free[j-1] + v veya -v
                # (hold dizileri zaten 'başlatma' durumunu içerdiği için max(hold...) yeterlidir)
                # Kapatınca 'cool' durumuna geçeriz, bu adımda işlem biter.
                close_normal = max(hold_n[j], free[j-1]) + v
                close_short = max(hold_s[j], free[j-1]) - v
                new_cool[j] = max(close_normal, close_short)
                
                # --- Boşa Çıkma (Free) ---
                # Ya zaten boştaydık (free[j])
                # Ya da bekleme süresi (cool[j]) bitti, artık özgürüz.
                # cool[j] bir önceki adımdan (dünden) gelir.
                new_free[j] = max(free[j], cool[j])
            
            # Durumları güncelle
            free = new_free
            cool = new_cool
            hold_n = new_hold_n
            hold_s = new_hold_s
            
        # Sonuç: En fazla k işlem sonucunda boşta (free) veya son anda kapatmış (cool) durumdaki max kâr.
        return max(max(free), max(cool))