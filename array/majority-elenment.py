def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
"""
cách 2: sắp xếp rồi lấy phần tử n//2
def majority_element(nums):
    nums.sort()
    return nums[len(nums) // 2]

"""