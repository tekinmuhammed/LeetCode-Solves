class Solution:
    representative = [0 for i in range(26)]

    def find(self, x):
        # Return the representation of the component/character 'x'
        if self.representative[x] == x:
            return x

        self.representative[x] = self.find(self.representative[x])
        return self.representative[x]

    def performUnion(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if x < y:
            self.representative[y] = x
        else:
            self.representative[x] = y

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        for i in range(26):
            self.representative[i] = i
            
        for i in range(len(s1)):
            self.performUnion(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))

        ans = ""
        for c in baseStr:
            ans += chr(self.find(ord(c) - ord('a')) + ord('a'))

        return ans