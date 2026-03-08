def removeDuplicates(nums):
    pos = 1
    for i in range(1, len(nums)):
        if nums[pos-1] != nums[i]:
            nums[pos] = nums[i]
            pos += 1
    return pos