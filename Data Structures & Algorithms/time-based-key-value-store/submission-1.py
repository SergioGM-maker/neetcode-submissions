class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        sol = ""
        values = self.d[key]
        l= 0
        r= len(values)-1
        m = (l+r)//2

        while l <= r:
            if values[m][1] <= timestamp:
                sol = values[m][0]
                l = m+1
            else:
                r = m-1
            m = (l+r)//2

        return sol

        
