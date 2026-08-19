class Solution:
    from collections import deque
    def isValid(self, s: str) -> bool:
        closeopen={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack=[]
        for b in s:
            if b in closeopen:
                if len(stack) == 0:
                    return False
                top=stack.pop()
                if top != closeopen[b]:
                    return False
            else:
                stack.append(b)
        if len(stack) != 0:
            return False
        return True
        