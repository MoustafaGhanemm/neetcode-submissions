class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        curr_long = 0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set :
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            curr_long = max(curr_long, r - l + 1)
        return curr_long

            


        