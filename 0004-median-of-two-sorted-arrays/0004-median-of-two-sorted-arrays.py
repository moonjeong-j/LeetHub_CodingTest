class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li = nums1+nums2
        li=sorted(li)
        length = len(li)
        if length%2==0:
            middle = (li[length//2-1]+li[length//2])/2
        else:
            middle =li[(length+1)//2-1]
            
        return middle

        
        
        