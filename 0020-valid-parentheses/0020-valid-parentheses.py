class Solution:
    def isValid(self, s: str) -> bool:
        matching_bracket = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for char in s:
            if char in matching_bracket:
                if len(stack) > 0:
                    top_element = stack.pop()
                else:
                    top_element = '#'
                if top_element != matching_bracket[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0