class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        start = len(s1) - 1
        for r in range(start, len(s2)):
            if sorted(s2[l:r + 1]) == sorted(s1):
                return True
            l += 1
        return False

