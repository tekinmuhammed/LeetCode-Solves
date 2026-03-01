class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        # Verilen n stringi içindeki her bir karakteri (rakamı) gez,
        # en büyük olanı bul ve tamsayıya çevirerek döndür.
        # Örneğin n = "82734" ise içindeki en büyük rakam 8'dir.
        # Bu durumda en az 8 tane deci-binary sayıya ihtiyaç duyulur.
        return int(max(n))