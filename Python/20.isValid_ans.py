def isValid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack
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