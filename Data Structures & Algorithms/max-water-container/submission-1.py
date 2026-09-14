class Solution:

    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maximum = 0

        while right > left:

            if min(heights[right],heights[left]) * (right-left) > maximum:
                maximum= min(heights[right],heights[left]) * (right-left)

            if heights[left]>heights[right]:
                right = right-1
            else:
                left = left+1


        return maximum