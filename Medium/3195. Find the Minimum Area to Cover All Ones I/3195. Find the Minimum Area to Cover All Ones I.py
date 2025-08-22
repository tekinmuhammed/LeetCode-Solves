class Solution:
    def minimumArea(self, g: List[List[int]]) -> int:
        f = lambda g,q:next(k for k in range(len(g))[::q] if any(g[k]))
        return (f(g,-1)-f(g,1)+1)*(f(g:=[*zip(*g)],-1)-f(g,1)+1)