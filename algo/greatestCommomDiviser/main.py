
def greatestCommomDiviser(array):
    div = 2
    count = 0

    for num in array:
        if num % div != 0:
            div += 1

        if num % div == 0:
            count += 1

        if count == len(array):
            break

    if count < len(array):
        div = 1


if __name__ == '__main__':
    r1 = greatestCommomDiviser([4, 6, 8])
    r2 = greatestCommomDiviser([3, 6, 9])
    r3 = greatestCommomDiviser([18, 45])
    print(r1)
    print(r2)
    print(r3)
