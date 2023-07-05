class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x=nums1+nums2
        x.sort()
        a=len(x)
        if(a%2==0):
            y=x[(a/2)-1]+x[a/2]
            return y*0.5
        else:
            return x[(a-1)/2]
