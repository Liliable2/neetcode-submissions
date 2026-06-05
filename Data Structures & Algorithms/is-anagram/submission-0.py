class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram requires equal length
        if len(s) != len(t):
            return False
        
        # count frequencies using hashmap equivalence
        # this models how the core property of anagram works
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            # s[i] gives the char
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        return count_s == count_t

