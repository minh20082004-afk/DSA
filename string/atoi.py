class Solution(object):
    def myAtoi(self, s):

        i = 0
        n = len(s)
        sign = 1
        result = 0

        # 1. bỏ khoảng trắng đầu
        while i < n and s[i] == " ":
            i += 1

        # 2. kiểm tra dấu
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. đọc các chữ số
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result = result * sign

        # 4. giới hạn 32 bit
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result