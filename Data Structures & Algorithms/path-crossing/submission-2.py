class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        seen.add((0,0))

        ns, we = 0,0
        for char in path:
            if char == "N":
                ns += 1
            elif char == "S":
                ns -= 1
            elif char == "W":
                we -= 1
            elif char == "E":
                we += 1
            
            curr = (ns,we)
            if curr in seen:
                return True
            seen.add(curr)
        return False
        