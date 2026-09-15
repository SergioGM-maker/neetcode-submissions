class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sol = ""
        checklist = {}
        for i in t:
            checklist[i] = 1 + checklist.get(i, 0)
        left = 0
        right = 0
        attempt = {}

        have, need = 0, len(checklist)
        res, resLen = [-1,-1], float("infinity")

        while left < len(s)-len(t)+1 and right < len(s):
            curr = s[right]


            attempt[curr] = 1 + attempt.get(curr, 0)
                    
            if curr in checklist and attempt[curr] == checklist[curr]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                attempt[s[left]] -= 1

                if s[left] in checklist and attempt[s[left]] + 1 == checklist[s[left]]:
                    have -=1
                
                left = left +1
                
                while left < len(s)-len(t)+1 and s[left] not in checklist:
                    left = left +1


            right = right + 1       


        
        return s[res[0] : res[1] + 1] if resLen != float("infinity") else ""
        
        