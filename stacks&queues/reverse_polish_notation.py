# Evaluate Reverse Polish Notation
# LeetCode 150: You are given an array of strings tokens that
# represents an arithmetic expression in Reverse Polish Notation
# (postfix). Evaluate the expression and return an integer.
#
# Valid operators: +, -, *, /. Each operand is an integer.
# Division truncates toward zero. The input always represents a
# valid expression.
#
# Approach: Scan tokens left to right. Push numbers onto a stack.
# When you see an operator, pop the right operand first, then the
# left operand, apply the operator, and push the result back.
#
# Time: O(n) — each token is processed once; each number is pushed
#       and popped at most once.
# Space: O(n) — the stack can hold up to n numbers in the worst case.


class Solution:
    def calc(self, num1, num2, op):
        num1 = int(num1)
        num2 = int(num2)
        if op == '+':
            return num2 + num1
        elif op == '-':
            return num2 - num1
        elif op == '*':
            return num2 * num1
        elif op == '/':
            return int(num2 / num1)

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                new_num = self.calc(stack.pop(), stack.pop(), i)
                stack.append(new_num)
            else:
                stack.append(i)
        return int(stack.pop())
