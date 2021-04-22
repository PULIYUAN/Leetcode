#4.18
def romanToInt(R: str):
    RtI = {'I':1,'IV':4,'IX':9,'V':5, 'X':10,'XL':40,'XC':90, 'L':50, 'C':100, 'CD':400,'CM':900,'D':500, 'M':1000}
    I = []
    i = 0
    #得到数字序列再求和
    while i < len(R):
        key_1 = R[i:i+1]
        key_2 = R[i:i+2]
        if key_2 in RtI:
            I.append(RtI.get(key_2))
            i += 2
        else:
            I.append(RtI.get(key_1))
            i += 1
    return sum(I)
print(romanToInt("CMXCIX"))
print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))