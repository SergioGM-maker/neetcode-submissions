class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        road = list(zip(position,speed))
        road.sort()
        road.reverse()
        for car in road:
            time_remaining = car[1]/(target-car[0])
            if stack == [] or time_remaining < stack[-1]:
                stack.append(time_remaining)
        return len(stack)