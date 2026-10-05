class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        nstart, nend = newInterval
        for i in range(len(intervals)):
            start1, end1 = intervals[i]
            if nend  < start1 : 
                res.append(newInterval)
                return res + intervals[i:]
            elif nstart > end1:
                res.append(intervals[i])
            else: 
                nstart, nend = [min(start1,nstart), max(end1,nend)]
                newInterval = [nstart,nend]
        res.append(newInterval)
        return res
            
    
            
            