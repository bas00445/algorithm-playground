def palindrome(number):
    if number < 0:
        return False

    numStr = str(number)

    isPalin = False

    for i in range(len(numStr)):
        if (numStr[i] == numStr[len(numStr) - 1 - i]):
            isPalin = True
        else:
            return False

    return isPalin


if __name__ == '__main__':
    r1 = palindrome(100)
    r2 = palindrome(121)
    print(r1)
    print(r2)
