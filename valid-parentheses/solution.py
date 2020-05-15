def valid_parentheses(string):
    stack = []
    for c in string:
        if (c == '('):
            stack.append('(')
        elif (c == ')'):
            if (len(stack) == 0):
                return False
            else:
                stack.pop()
    return len(stack) == 0