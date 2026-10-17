class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        odd = False
        firstHalf= 0
        if l%2 != 0:
            odd = True

        
        l = l//2

        p1 = 0
        p2 = 0
        x= 0
        while x<l:
            x += 1
            if  p2 == len(nums2) or (
                p1 != len(nums1) and 
                nums1[p1] < nums2[p2]) :
                
                if not odd:
                    firstHalf = nums1[p1]

                p1 += 1
            else:
                if not odd:
                    firstHalf = nums2[p2]
                p2 += 1
        
        
        secondHalf = 0

        if p1 == len(nums1):
            secondHalf = nums2[p2]
        elif p2 == len(nums2):
            secondHalf = nums1[p1]
        else:
            secondHalf = min(nums1[p1],nums2[p2])
        
        if odd:
            return secondHalf
        else:
            return (firstHalf+secondHalf) / 2

        
            
        