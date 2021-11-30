from z1 import Stack


def determ_balance(brace):
    opening = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    if brace[0] in ')}]':
        return 'несбалансированно'
    else:
        for bracket in brace:
            if bracket in '([{':
                stack.push(bracket)
                # print('push', stack)
            elif bracket in ')}]':
                last = stack.peek()
                if last == opening[bracket]:
                    stack.pop()
                else:
                    return "несбалансированно"
    if stack.is_empty() == True:
        return "сбалансированно"


print(determ_balance('{{[()]}}'))