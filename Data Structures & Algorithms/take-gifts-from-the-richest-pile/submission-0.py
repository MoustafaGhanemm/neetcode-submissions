import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        
        heap = []
        for g in gifts:
            heap.append(-g)   # negate so the min-heap acts like a max-heap
        heapq.heapify(heap)
        for i in range(k):
            n = -heapq.heappop(heap)
            heapq.heappush(heap, (-math.floor(math.sqrt(n))))
        
        return -sum(heap)




        print(gifts)