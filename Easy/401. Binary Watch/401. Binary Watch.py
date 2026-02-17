class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        times = []
        
        # Saatler 0-11 arası olabilir (12 saatlik dilim)
        for h in range(12):
            # Dakikalar 0-59 arası olabilir
            for m in range(60):
                
                # Saat ve dakikanın binary karşılıklarındaki '1' sayısını hesapla.
                # bin(h) örneğin '0b101' döner, count('1') ile içindeki 1'leri sayarız.
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    
                    # Zamanı istenen formata çevir.
                    # f"{h}:{m:02d}" -> Saat olduğu gibi, dakika ise 2 haneli olacak şekilde (gerekirse başına 0 ekler).
                    times.append(f"{h}:{m:02d}")
                    
        return times