class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        content = {}
        sol = 0
        while right < len(s):
            if content.get(s[right]) is None:
                content.update({s[right]:1})
            else:
                content.update({s[right]:content.get(s[right])+1})
                # window size - most repeated character <= substitutions
            
            while (right - left + 1 - max(content.values())) > k:
                content.update({s[left]:content.get(s[left])-1})
                left = left+1
            
            sol = max(right-left+1,sol)
            right = right +1


        return sol