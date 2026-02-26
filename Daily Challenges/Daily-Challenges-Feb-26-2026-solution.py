# 🔐 LeetCode 1404. Number of Steps to Reduce a Number in Binary Representation to One

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 1404](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/)

# 🧠 Problem Description
# [Github LeetCode 1404. Number of Steps to Reduce a Number in Binary Representation to One](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/1404.%20Number%20of%20Steps%20to%20Reduce%20a%20Number%20in%20Binary%20Representation%20to%20One)

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