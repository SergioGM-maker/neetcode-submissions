class KthLargest:
    

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        self.k = k
        

    def add(self, val: int) -> int:
        # l = 0
        # r = len(nums)-1
        # while 
        self.arr.append(val)
        self.arr.sort()

        return self.arr[-self.k]
