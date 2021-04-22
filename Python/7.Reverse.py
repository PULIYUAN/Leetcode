# 执行用时：40 ms, 在所有 Python3 提交中击败了77.74%的用户
# 内存消耗：14.7 MB, 在所有 Python3 提交中击败了86.01%的用户

def reverse(x: int) -> int:
    r = []
    p = ''
    #    if x >= -2 ** 31 and x <= 2 ** 31 - 1:
    l = list(str(x))
    while l:
        s = l.pop()
        r.append(s)
    if r[-1] == '-':
        r.pop()
        for i in r:
            p += i
            result = -int(p)
    else:
        for i in r:
            p += i
            result = int(p)
    if result < -2 ** 31 or result > 2 ** 31 - 1:
        result = 0
    return result

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))
print(reverse(1534236469))
