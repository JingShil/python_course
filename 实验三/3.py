def valid_braces(string):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in string:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack