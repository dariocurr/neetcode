class Solution:
    def isValid(self, s: str) -> bool:
        comps = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in "{[(":
                stack.append(c)
            else:
                if stack:
                    value = stack.pop()
                    comp = comps[c]
                    if value != comp:
                        return False
                else:
                    return False
        return len(stack) == 0

        