class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # you need to split them by slash
        contents = path.split('/')
        stack = []

        for c in contents:
            if c == "" or c == ".":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return '/' + '/'.join(stack)