class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        anagram = {}
        for s in s1:
            if anagram.get(s) is None:
                anagram.update({s:1})
            else:
                anagram.update({s:anagram.get(s)+1})
        
        i = 0
        window = {}
        while i < len(s1) and i < len(s2):
            if window.get(s2[i]) is None:
                window.update({s2[i]:1})
            else:
                window.update({s2[i]:window.get(s2[i])+1})

            i = i+1    

        if window == anagram:
            return True  

        i = 0
        j = len(s1)
        while j < len(s2):
            if window.get(s2[j]) is None:
                window.update({s2[j]:1})
            else:
                window.update({s2[j]:window.get(s2[j])+1})
            window.update({s2[i]:window.get(s2[i])-1})
            if window.get(s2[i]) == 0:
                window.pop(s2[i])



            if window == anagram:
                return True 
            j = j+1
            i = i+1 


        return False