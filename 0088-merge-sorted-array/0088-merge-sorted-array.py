class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        length_of_num1 = m
        length_of_num2 = n
        
        pointer1 = m - 1 # cause in array its starts from 0..so at the end to access you need to be -1
        pointer2 = n - 1
        pointer_merged = m + n - 1
        
        while pointer1 >= 0 and pointer2 >= 0: 
            # you need to loop run until there are elements
            if nums1[pointer1] > nums2[pointer2]:
                # if the last element of in 1st array is larger than the seconf one
                # add it to the last of the array
                nums1[pointer_merged] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[pointer_merged] = nums2[pointer2]
                pointer2 -= 1
            pointer_merged -= 1
            
        while pointer2 >= 0:
            nums1[pointer_merged] = nums2[pointer2]
            pointer2 -= 1
            pointer_merged -= 1
            
        
        
        
        