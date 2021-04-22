#两数之和 two-sum
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
'''
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            #if i!=j:
            if nums[i]+nums[j] == target:
                return[i,j]
    return []
#O(n^2)  O（1）
nums = [2, 4, 4, 15]
target = 8
result = twoSum(nums, target)
print(result)

###超时！