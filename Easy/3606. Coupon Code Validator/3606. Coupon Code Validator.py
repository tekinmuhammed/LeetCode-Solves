class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        import re

        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        order = {name: i for i, name in enumerate(valid_lines)}
        pattern = re.compile(r'^[A-Za-z0-9_]+$')

        valid_coupons = []

        for c, b, a in zip(code, businessLine, isActive):
            if not a:
                continue
            if not c or not pattern.match(c):
                continue
            if b not in order:
                continue
            valid_coupons.append((order[b], c))

        # Önce businessLine sırası, sonra code lexicographical
        valid_coupons.sort(key=lambda x: (x[0], x[1]))

        return [c for _, c in valid_coupons]