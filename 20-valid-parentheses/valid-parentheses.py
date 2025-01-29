class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = [] # thats our stack
        
        for char in s:
            if char in map: # need to check if there's closing bracket
                top_one = stack.pop() if stack else '#'
                if top_one != map[char]:
                    return False
            else:
                stack.append(char)

        return not stack
        