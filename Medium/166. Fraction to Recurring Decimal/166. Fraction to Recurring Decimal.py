class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        res = []

        # İşaret kontrolü
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        # Mutlak değerler ile işlem
        numerator, denominator = abs(numerator), abs(denominator)

        # Tam kısım
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)

        res.append(".")

        # Ondalık kısım için kalanları sakla (repeating detect)
        seen = {}
        while remainder != 0:
            if remainder in seen:
                res.insert(seen[remainder], "(")
                res.append(")")
                break

            seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(res)