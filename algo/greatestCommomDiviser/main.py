
def greatestCommomDiviser(a, b):
    if b == 0:
        return a
    return greatestCommomDiviser(b, a % b)


if __name__ == '__main__':
    r1 = greatestCommomDiviser(4, 8)
    r2 = greatestCommomDiviser(2, 3)
    print(r1)
    print(r2)
