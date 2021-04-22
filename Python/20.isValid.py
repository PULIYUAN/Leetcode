# 数量对 要匹配 顺序对
# def isValid(s: str) -> bool:
#     flag1 = 1
#     flag2 = 0
#     s1 = []
#     s2 = []
#     s3 = []
#     if s[len(s) // 2 - 1] == '(':
#         if s[len(s) // 2] != ')':
#             flag1 = 0
#     if s[len(s) // 2 - 1] == '[':
#         if s[len(s) // 2] != ']':
#             flag1 = 0
#     if s[len(s) // 2 - 1] == '{':
#         if s[len(s) // 2] != '}':
#             flag1 = 0
#     for i in s:
#         if i == '(':
#             s1.append(0)
#         elif i == ')':
#             if not s1:
#                 return False
#             else:
#                 s1.pop()
#         elif i == '{':
#             s2.append(0)
#         elif i == '}':
#             if not s2:
#                 return False
#             else:
#                 s2.pop()
#         elif i == '[':
#             s3.append(0)
#         elif i == ']':
#             if not s3:
#                 return False
#             else:
#                 s3.pop()
#         else:
#             pass
#     if not s1 and not s2 and not s3:
#         flag2 = 1
#     else:
#         flag2 = 0
#     return bool(flag1 and flag2)
# print(isValid("[([]])"))失效

# 成对消去——堆栈(先进的必须先出)
def isValid(s: str) -> bool:
    s1 = []
    count1 = 0
    count2 = 0
    if s[0] == ')' or s[0] == ']' or s[0] == '}':
        return False
    if len(s) % 2 != 0:
        return False
    else:
        for i in s:
            if i == ')' or i == ']' or i == '}':
                count1 += 1
            else:
                count2 += 1
        if count1 != count2:
            return False
        else:
            for i in range(len(s)):
                if s[i] == '(' or s[i] == '[' or s[i] == '{':
                    s1.append(s[i])
                else:
                    if not s1:
                        return False
                    else:
                        if s[i] == ')' and s1[-1] == '(':
                            s1.pop()
                        elif s[i] == ']' and s1[-1] == '[':
                            s1.pop()
                        elif s[i] == '}' and s1[-1] == '{':
                            s1.pop()
                        else:
                            pass
            if s1:
                return False
            else:
                return True


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("{[]}"))
print(isValid("{()()}"))
print(isValid("([)]"))
print(isValid("[([]])"))
print(isValid("(){}}{"))
print(isValid("([}}])"))
print("over")
