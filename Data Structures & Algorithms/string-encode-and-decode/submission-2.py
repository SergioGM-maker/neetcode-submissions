class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        if strs == []:
            sol = "º"
        else:
            sol = "ñ".join(strs)
        return sol
    
    def decode(self, s: str) -> List[str]:
        if s!= "º":
            return s.split("ñ")
        else:
            return []