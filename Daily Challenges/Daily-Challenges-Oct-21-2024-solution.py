# LeetCode 1106 - Parsing A Boolean Expression

# 🔗 Problem Link
#[LeetCode 1106 - Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/)

# 🧠 Problem Description
#[Github LeetCode 1106 - Parsing A Boolean Expression](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Hard/1106.%20Parsing%20A%20Boolean%20Expression)

class Solution(object):
    def parseBoolExpr(self, expression):
        def evalExpr(expr):
            if expr == 't':
                return True
            if expr == 'f':
                return False
        def parse(expression):
            if expression[0] == '!':
                return not parse(expression[2:-1])
            elif expression[0] == '&':
                parts = splitSubExpr(expression[2:-1])
                return all(parse(part) for part in parts)
            elif expression[0] == '|':
                parts = splitSubExpr(expression[2:-1])
                return any(parse(part) for part in parts)
            else:
                return evalExpr(expression)
        def splitSubExpr(expr):
            parts = []
            balance = 0
            last = 0
            for i, c in  enumerate(expr):
                if c == '(':
                    balance += 1
                elif c == ')':
                    balance -= 1
                elif c == ',' and balance == 0:
                    parts.append(expr[last:i])
                    last = i + 1
            parts.append(expr[last:])
            return parts
        return parse(expression)

solution = Solution()
expression = "&(|(!(f)))"
print(solution.parseBoolExpr(expression))