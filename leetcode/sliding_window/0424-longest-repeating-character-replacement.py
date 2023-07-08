class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} 
        l = 0 
        res = 0 
        maxf = 0 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1 
                l += 1 
            res = max(res, (r - l + 1))
        return res

#O(n)
'''
https://leetcode.com/problems/longest-repeating-character-replacement/
----------------------------------------------------------------------



'''