class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        # Olayları işlem sırasına sokmak için yeni bir liste oluşturuyoruz.
        # Sıralama önceliği:
        # 1. Zaman (timestamp) - Artan sırada
        # 2. Olay Türü - Aynı zamanda ise OFFLINE önce işlenmeli.
        #    Bunun için OFFLINE'a 0, MESSAGE'a 1 değeri veriyoruz.
        
        processed_events = []
        for event in events:
            event_type = event[0]
            timestamp = int(event[1])
            
            # Sıralama için 'rank' belirle: OFFLINE önce gelmeli
            rank = 0 if event_type == "OFFLINE" else 1
            
            # (Zaman, Öncelik, Orijinal Veri)
            processed_events.append((timestamp, rank, event))
        
        # Listeyi sırala
        processed_events.sort()

        # Sonuç dizisi: Her kullanıcının mention sayısı
        mentions = [0] * numberOfUsers
        
        # online_time[i]: i. kullanıcının tekrar çevrimiçi olacağı zamanı tutar.
        # Başlangıçta hepsi 0 (yani hepsi çevrimiçi).
        online_time = [0] * numberOfUsers

        for ts, rank, event in processed_events:
            event_type = event[0]
            
            if event_type == "OFFLINE":
                user_id = int(event[2])
                # Kullanıcı 60 birim süreyle çevrimdışı kalacak.
                # Tekrar çevrimiçi olma zamanı: ts + 60
                # Not: Soru, OFFLINE olayının sadece çevrimiçi kullanıcılara geleceğini garanti eder.
                online_time[user_id] = ts + 60
            
            elif event_type == "MESSAGE":
                mention_string = event[2]
                
                if mention_string == "ALL":
                    # 'ALL': Çevrimiçi/çevrimdışı fark etmeksizin herkesi say
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                        
                elif mention_string == "HERE":
                    # 'HERE': Sadece şu an çevrimiçi olanları say
                    for i in range(numberOfUsers):
                        # Eğer şimdiki zaman >= tekrar çevrimiçi olma zamanı ise kullanıcı çevrimiçidir.
                        if ts >= online_time[i]:
                            mentions[i] += 1
                            
                else:
                    # Belirli ID'leri işle (örn: "id0 id1 id0")
                    ids = mention_string.split()
                    for id_str in ids:
                        # "id" öneki hariç sayıyı al (örn: "id10" -> 10)
                        uid = int(id_str[2:])
                        mentions[uid] += 1
                        
        return mentions