import math


def reverseInteger(num):
    unit = 0
    value = 0

    absNum = abs(num)
    numString = str(absNum)

    for i in range(len(numString) - 1, -1, -1):
        if numString[i] == '0':
            unit += 1
            continue

        value += int(numString[i]) * math.pow(10, len(numString) - unit - 1)
        unit += 1

    result = int(value)
    result = 0 if (result > math.pow(2, 31) - 1 or result <
                   math.pow(-2, 31)) else result

    return result if num > 0 else -result


if __name__ == '__main__':
    r1 = reverseInteger(123)
    r2 = reverseInteger(-123)
    r3 = reverseInteger(120)
    r4 = reverseInteger(0)

    print(r1)
    print(r2)
    print(r3)
    print(r4)
