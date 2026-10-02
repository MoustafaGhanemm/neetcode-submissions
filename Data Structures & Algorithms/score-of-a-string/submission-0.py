class Solution:
    def scoreOfString(self, s: str) -> int:
        sumy = 0

        i = 0
        while i < len(s) - 1 and i + 1 <= len(s) - 1:
            sumy += abs(ord(s[i]) - ord(s[i+1]))
            print(ord(s[i]), ord(s[i+1]))
            i+= 1
        
        return sumy

            
