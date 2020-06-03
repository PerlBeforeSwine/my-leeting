class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        prefix = min(strs, key=len)
        
        
        for word in strs:
            i = 0
            if word == "" or prefix == "":
                return ""
            if word[i] != prefix[i]:
                return ""
            while i < len(prefix):
                if prefix[i] == word[i]:
                    i += 1
                    continue
                else:
                    prefix = prefix[:i]
                    break
        
        return prefix