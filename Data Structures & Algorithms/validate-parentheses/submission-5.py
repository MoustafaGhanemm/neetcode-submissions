class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {"]":"[",
        ")":"(",
        "}":"{"}

        stack = []

        for p in s:
            if p in p_dict:  
                if not stack or stack[-1] != p_dict[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)
        return len(stack) == 0
        

                