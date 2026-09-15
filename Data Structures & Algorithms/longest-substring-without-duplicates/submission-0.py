class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maximum = 0
        bag = set()
        while right < len(s):
            while s[right] in bag:
                bag.discard(s[left])
                left = left+1
            bag.add(s[right])
            maximum = max(maximum, len(bag))
            right = right +1

        return maximum
        