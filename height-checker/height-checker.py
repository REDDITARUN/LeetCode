class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        na = sorted(heights)
        c = 0
        print(na)
        for i in range(len(heights)):
            if na[i] != heights[i]:
                c+=1
        return c
        
#         seen = heights[0]
#         print(seen)

#         for i in range(len(heights)):
#             seen = max(seen,heights[i])
#             if heights[i] < seen or heights[i] > heights[i+1]:
#                 c+=1
            
#         return c

                
            
                
        