def validParentheses(string):
    stack = []
    closeToOpen = {')': '(', '}': '{', ']': '['}

    for s in string:
        if s in closeToOpen:
            if len(stack) > 0 and stack[-1] == closeToOpen[s]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s)

    return True if len(stack) == 0 else False


if __name__ == "__main__":
    print(validParentheses("[[]]"))
    print(validParentheses("[[]}"))
