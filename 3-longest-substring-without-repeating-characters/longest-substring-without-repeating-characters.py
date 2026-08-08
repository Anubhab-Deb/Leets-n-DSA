class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        
        word=[]
        for i in range(len(s)):
            char=set()
            for j in range(i, len(s)):
                old_len=len(char)
                char.add(s[j])
                if len(char)==old_len:
                    break
                
            else:    
                j+=1    
            word.append(s[i:j])
        longest=max(word, key=len)
        return len(longest)