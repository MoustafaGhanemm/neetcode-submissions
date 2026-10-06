class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = []
        ls, le = intervals[0]
        for i in range(1, len(intervals)):
            s1, e1 = intervals[i]
            

            if le <  s1:
                res.append([ls,le])
                ls, le = s1, e1
                continue
            elif s1 <= le:
                ls, le = min(ls, s1), max(le, e1)
            
        res.append([ls, le])
        return res

            
