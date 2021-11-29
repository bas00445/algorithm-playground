def findMostAppearanceInString(string):
    collections = {}

    for s in string:
        if s not in collections:
            collections[s] = 1
        else:
            collections[s] = collections[s] + 1

    values = list(collections.values())
    maxValueIndex = values.index(max(values))

    return list(collections)[maxValueIndex], max(values)


if __name__ == "__main__":
    r = findMostAppearanceInString("HELLOOOOWORLD")
    print(r)
