def twoSum(nums, target):
    # Assume num in nums is unique
    for i in range(0, len(nums)):
        left = target - nums[i]
        others = nums[i+1: len(nums)]

        if (left in others):
            return [nums[i], nums[others.index(left) + (i+1)]]

    return []


def threeSum(nums):
    target = 0
    result = []

    for i in range(len(nums)):
        left = target - nums[i]
        pair = twoSum(nums[i+1:len(nums)], left)

        if pair:
            temp = [nums[i]] + pair
            result.append(temp)

    return result


if __name__ == '__main__':
    r1 = threeSum([-1, 0, 1, 2, -1, -4])
    print(r1)
