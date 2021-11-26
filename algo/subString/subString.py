def subString(string, target):
    if len(string) < len(target):
        return False

    for i in range(0, len(string)):
        count = 0
        for j in range(0, len(target)):
            if target[j] == string[i]:
                count += 1
                i += 1
                j += 1

            if count == len(target):
                return True

    return False


def main():
    r1 = subString("HELLOWORLD", "RL")
    r2 = subString("HELLOWORAL", "RL")
    r3 = subString("HELLOWORAL", "X")
    r4 = subString("H", "H")
    r5 = subString("HE", "H")
    r6 = subString("HE", "HER")
    r7 = subString("HER", "")

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(r7)


main()
