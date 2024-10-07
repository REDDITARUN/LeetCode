class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        max_elm = max(arr)
        index_m = arr.index(max_elm)
        c = 0
        
        if len(arr) < 3:
            return False
        
        # If the peak is at the beginning or the end, it's not a valid mountain
        if index_m == 0 or index_m == len(arr) - 1:
            return False
        
        
        for i in range(1, index_m):
            if arr[i] <= arr[i-1]:
                return False
            
        for j in range(index_m+1, len(arr)):
            if arr[j] >= arr[j-1]:
                return False

        return True
            
            
        