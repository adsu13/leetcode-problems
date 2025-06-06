def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    reversed_num = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x != 0:
        digit = x % 10
        x = x // 10
        if (sign == 1 and reversed_num > (INT_MAX - digit) // 10) or \
           (sign == -1 and -reversed_num < (INT_MIN + digit) // 10 + 1):
            return 0
        reversed_num = reversed_num * 10 + digit
    return sign * reversed_num