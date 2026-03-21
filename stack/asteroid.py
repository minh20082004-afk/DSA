class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(ast):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                break
            else:
                stack.append(ast)

        return stack
    # lệnh while-else: nếu điều kiện while không được thì sẽ chạy else. Hàm else sẽ chạy được khi không được kết thúc bằng break.