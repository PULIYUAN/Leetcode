def isPalindrome(x: int) -> bool:
    r = list(str(x))
    s = list(str(x))
    r.reverse()
    return r == s


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
