class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == '+':
                stack.append(stack.pop() + stack.pop())
            elif ch == '-':
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif ch == '*':
                stack.append(stack.pop() * stack.pop())
            elif ch == '/':
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else: 
                stack.append(int(ch))

        return stack[-1]