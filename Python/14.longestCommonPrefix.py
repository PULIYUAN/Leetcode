def lcp(str1, str2):  # 提取两个字符串最长前缀
    i = min(len(str1), len(str2))
    index = 0
    while index < i:
        if str1[index] == str2[index]:
            index += 1
        else:
            break
    return str1[:index]

def longestCommonPrefix(strs) -> str:
    if not strs:
        return ''
    prefix = strs[0]
    for str in strs:
        prefix = lcp(prefix,str)
        if not prefix:
            break
    return prefix

strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
#print(lcp("flower", "flow"))
print(longestCommonPrefix(strs1))
print(longestCommonPrefix(strs2))
print('over')
