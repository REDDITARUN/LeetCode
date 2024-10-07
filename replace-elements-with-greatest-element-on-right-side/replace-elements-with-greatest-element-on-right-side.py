class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if len(arr)==1:
            arr[0] = -1
            return arr
        
        max_right = -1
        
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            
            arr[i] = max_right
            
            max_right = max(current,max_right)
            
        return arr
            
            
        