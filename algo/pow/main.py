

def pow(x, n):
    if n == 0:
        return 1

    res = x

    for i in range(abs(n) - 1):
        res *= x

    if n < 0:
        res = 1/res

    return res


if __name__ == "__main__":
    r = pow(2, 5)
    r2 = pow(1.4, 10)
    r3 = pow(5, -4)
    print(r)
    print(r2)
    print(r3)
