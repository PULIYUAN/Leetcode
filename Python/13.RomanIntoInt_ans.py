def romanToInt(s: str) -> int:
    d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
         'CM': 800, 'M': 1000}
    result = 0
    for i, n in enumerate(s):
        str1 = s[max(i - 1, 0):i + 1]
        if str1 in d:
            result += d.get(str1)
        else:
            result += d[n]
    return result
print(romanToInt("CMXCIX"))
print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))