class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f=None #3
        s=None
        t=None

        
        for num in nums:
            if num == f or num == s or num == t:
                continue
            
            if f is None or num>f:
                t = s
                s = f
                f = num
            elif  s is None or num > s:
                t = s
                s = num
            elif t is None or num>t:
                t =num
        
        print(f,s,t)
        if t ==None:
            return f
        else:
            return t
            
        