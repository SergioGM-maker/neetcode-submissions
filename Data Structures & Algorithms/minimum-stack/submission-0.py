class Node:
    
    def __init__(self, value: int, min: int, next):
        self.value = value
        self.min = min
        self.next = next




class MinStack:

    def __init__(self):
        self.head = None
        

    def push(self, val: int) -> None:
        if not self.head:
            self.head = Node(val,val,None)
        else:
            self.head = Node(val,min(val,self.head.min),self.head)

    def pop(self) -> None:
        if self.head != None:
            self.head = self.head.next
        

    def top(self) -> int:
        if self.head != None:
            return self.head.value
        else: 
            return -9999
        

    def getMin(self) -> int:
        
        if self.head != None:
            return self.head.min
        else: 
            return -9999
        
