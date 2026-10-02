class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count_r = Counter(ransomNote)
        print(count_r)

        for char in magazine:
            if char in count_r and count_r[char] != 0:
                count_r[char] -= 1
        
        for key,value in count_r.items():
            if value == 0:
                continue
            else:
                return False
        return True


        

        
        