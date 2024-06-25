def valid_parentheses(parens):
    stack = []
    
    pair_map = {')': '('}
    
    for char in parens:
        if char == '(':
            stack.append(char)
        elif char == ')' and len(stack) > 0 and stack[-1] == pair_map[char]:
            stack.pop()
        else:
            return False
    
    return len(stack) == 0

