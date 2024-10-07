class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        na = []
        l = len(arr)
        for i in range(l):
            if arr[i] != 0:
                na.append(arr[i])
            elif arr[i] == 0:
                na.append(0)
                na.append(0)
                
            if len(arr) == len(na):
                break
                
        for i in range(l):
            arr[i] = na[i]
        
        return arr
        