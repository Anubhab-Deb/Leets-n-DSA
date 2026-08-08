class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        for i in range(len(s)):
            word=""
            for j in range(i, len(s)):
                if s[j] in word:
                    break
                else:
                    word+=s[j]
            longest=max(longest, len(word))
        return longest