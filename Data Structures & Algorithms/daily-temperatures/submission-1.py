class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if stack and stack[-1][0] < t:
                while stack and stack[-1][0] < t:
                    output[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append([t,i])
            else:
                stack.append([t,i])
        
        return output