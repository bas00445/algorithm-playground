def findMostAppearanceInString(string):
    datas = []

    for i in range(0, len(string)):
        count = 1
        for j in range(i+1, len(string)):
            if (string[i] == string[j]):
                count += 1

        datas.append(count)

    maxAppear = max(datas)
    maxIndex = datas.index(maxAppear)

    return string[maxIndex]


if __name__ == "__main__":
    r = findMostAppearanceInString("HELLOWORLD")
