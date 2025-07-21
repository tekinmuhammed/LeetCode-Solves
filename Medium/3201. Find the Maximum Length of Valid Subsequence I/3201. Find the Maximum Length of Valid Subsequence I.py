class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        mx = 0
        cnt = 0
        for e in nums:
            if e % 2 == 0:
                cnt += 1
            else:
                continue
        
        mx = max(mx, cnt)

        cnt = 0
        for e in nums:
            if e % 2 == 1:
                cnt += 1
            else:
                continue
        
        mx = max(mx, cnt)

        print(mx)

        flag = True

        cnt = 0
        for e in nums:
            if flag:
                if e % 2 == 1:
                    cnt += 1
                    flag = False
                else:
                    continue
            else:
                if e % 2 == 0:
                    cnt += 1
                    flag = True
                else:
                    continue
        
        mx = max(mx, cnt)
        
        flag = False

        cnt = 0
        for e in nums:
            if flag:
                if e % 2 == 1:
                    cnt += 1
                    flag = False
                else:
                    continue
            else:
                if e % 2 == 0:
                    cnt += 1
                    flag = True
                else:
                    continue
        
        mx = max(mx, cnt)

        return (mx)