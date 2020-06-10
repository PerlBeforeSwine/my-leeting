class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        if len(s) %2 != 0:
            return False
            
        brackets = {"[":"]","(":")","{":"}"}
        
        if s[0] in brackets.values():
            return False
        if s[len(s)-1] in brackets.keys():
            return False

        i = 0
        stack = []
        
        for i in range (0, len(s)):
            if s[i] in brackets.keys():
                stack.append(s[i])
            else: 
                if len(stack) == 0:
                    return False
                elif brackets[stack.pop()] != s[i]:
                    return False
        
        return len(stack) == 0
                    