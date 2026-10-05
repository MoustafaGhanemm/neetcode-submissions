class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        my_heap = []

        x1, y1 = 0, 0
        for p in points:
            x2, y2 = p     
            print(x1,x2,y1,y2)  
            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            heapq.heappush(my_heap, (dist, p))
        
        output = []
        for i in range(k):
            x, y = heapq.heappop(my_heap)
            output.append(y)
        
        return output