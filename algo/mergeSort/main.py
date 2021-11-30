def mergeTwoSortedList(listA, listB):
    sortedList = []

    lenA = len(listA)
    lenB = len(listB)

    i = j = 0

    while i < lenA and j < lenB:
        if listA[i] < listB[j]:
            sortedList.append(listA[i])
            i += 1
        else:
            sortedList.append(listB[j])
            j += 1

    # Handle case length of A or B are not equal
    while i < lenA:
        sortedList.append(listA[i])
        i += 1

    while j < lenB:
        sortedList.append(listB[j])
        j += 1
    # End: Handle case length of A or B are not equal

    return sortedList


def mergeSort(array):
    if len(array) <= 1:
        return array

    midIndex = len(array) // 2

    left = array[:midIndex]
    right = array[midIndex:]

    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)

    return mergeTwoSortedList(sortedLeft, sortedRight)


if __name__ == "__main__":
    a = [7, 15, 20]
    b = [8, 9]

    res = mergeTwoSortedList(a, b)
    print(res)

    # ans = mergeSort(a)
    # print(ans)
