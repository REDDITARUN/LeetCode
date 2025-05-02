class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_num = max(candies)
        res = []

        for i in range(len(candies)):
            tval = candies[i] + extraCandies
            if tval >= max_num:
                res.append(True)
            elif tval < max_num:
                res.append(False)
        
        return res
        