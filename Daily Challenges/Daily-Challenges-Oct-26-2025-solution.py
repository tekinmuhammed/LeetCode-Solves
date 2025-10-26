# 🏦 LeetCode 2043. Simple Bank System

# **Difficulty:** Medium
# **Problem Link:** [LeetCode 2043](https://leetcode.com/problems/simple-bank-system/description/)

# 🧠 Problem Description
# [Github LeetCode 2043. Simple Bank System](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/2043.%20Simple%20Bank%20System)

class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            account1 > len(self.balance)
            or account2 > len(self.balance)
            or self.balance[account1 - 1] < money
        ):
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance) or self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True