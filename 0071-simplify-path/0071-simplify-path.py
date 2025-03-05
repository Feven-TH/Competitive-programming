class Solution:
    def simplifyPath(self, path: str) -> str:
        var = path.split('/')
        stack = []
        for v in var:
            if v != "" and v != '..' and v != '.' and v != "/":
                stack.append(v)
            elif v == "..":
                if len(stack) != 0:
                    stack.pop()
        return "/" + "/".join(stack)
