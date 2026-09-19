
class MinStack:

    def __init__(self):
        self.registry: list[tuple[int,int]] = []

    def push(self, val: int) -> None:
        if not self.registry:
            self.registry.append((val,val))
        else:
            self.registry.append((val,min(val,self.registry[-1][1])))

    def pop(self) -> None:
        if self.registry != None:
            self.registry.pop()
        

    def top(self) -> int:
        if self.registry != None:
            return self.registry[-1][0]
        else: 
            return -9999
        

    def getMin(self) -> int:
        
        if self.registry != None:
            return self.registry[-1][1]
        else: 
            return -9999
        
