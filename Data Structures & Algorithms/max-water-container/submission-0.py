class Solution:

    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maximum = 0
        check = 0

        while right > left:
            curr_cant = min(heights[right],heights[left]) * (right-left)

            if curr_cant > maximum:
                maximum= curr_cant

            if heights[left]>heights[right]:
                right = right-1
            else:
                left = left+1


        return maximum