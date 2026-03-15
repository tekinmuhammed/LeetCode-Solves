# 1622. Fancy Sequence

# **Difficulty:** Hard
# **Problem Link:** [LeetCode 1622](https://leetcode.com/problems/fancy-sequence/)

# 🧠 Problem Description
# [Github LeetCode 1622. Fancy Sequence](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1622.%20Fancy%20Sequence)

class Fancy(object):

    def __init__(self):
        self.MOD = 10**9 + 7
        self.arr = []
        self.mul = 1
        self.add = 0

    def append(self, val):
        inv = pow(self.mul, self.MOD - 2, self.MOD)
        stored = (val - self.add) % self.MOD
        stored = (stored * inv) % self.MOD
        self.arr.append(stored)

    def addAll(self, inc):
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m):
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx):
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % self.MOD