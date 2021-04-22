#两数之和 two-sum
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
'''
def twoSum(nums, target):
    #哈希表/散列表：一种由键值对组成的数据结构，速度快
    hashtable = dict() #创建一个字典
    #enumerate():返回[(index,num1),(index,num2)...]
    for i, num in enumerate(nums): 
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []
#时间复杂度：O(n)→O(1)  空间复杂度：O（N）
nums = [2, 4, 4, 15]
target = 8
result = twoSum(nums, target)
print(result)
