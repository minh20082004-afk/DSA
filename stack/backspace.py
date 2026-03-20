class Solution:
    def build(self, s):
        stack = []
        for c in s:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return "".join(stack)

    def backspaceCompare(self, s, t):
        return self.build(s) == self.build(t)