class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "€"
        sol = ""
        a= 0
        while a < len(strs)-1:
            
            sol += strs[a] + "ñ"
            a +=1
        sol += strs[a]
        return sol

    def decode(self, s: str) -> List[str]:
        if s == "€":
            return []
        return s.split("ñ")
