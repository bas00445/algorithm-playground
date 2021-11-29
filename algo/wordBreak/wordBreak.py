def wordBreak(s, wordDict):
    tempS = s
    copyWordDict = wordDict.copy()

    for word in wordDict:
        if word in tempS:
            copyWordDict.remove(word)
            tempS = tempS.replace(word, '')

    return True if len(copyWordDict) == 0 else False


if __name__ == '__main__':
    r1 = wordBreak("leetcode", ["leet", "code"])
    r2 = wordBreak("applepenapple", ["apple", "pen"])
    r3 = wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])

    print(r1)
    print(r2)
    print(r3)
