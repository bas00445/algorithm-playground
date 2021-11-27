# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):
#             if (nums[i] + nums[j] == target):
#                 return [i, j]

#     return []


def twoSum(nums, target):
    # Assume num in nums is unique
    for i in range(0, len(nums)):
        left = target - nums[i]

        others = nums[i+1: len(nums)]

        if (left in others):
            return [i, others.index(left) + (i+1)]

    return []


def main():
    r1 = twoSum([2, 7, 11, 15], 9)
    r2 = twoSum([2, 7, 11, 15], 26)
    r3 = twoSum([3, 7, 6], 9)
    r4 = twoSum([3, 2, 4], 6)
    r5 = twoSum([3, 3, 4], 6)

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)


main()
