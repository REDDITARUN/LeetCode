class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        length = len(flowerbed)
        if n == 0:
            return True

        for i in range(length):
            prev = 0 if i == 0 else flowerbed[i-1]
            curr = flowerbed[i]
            next = 0 if i == length - 1 else flowerbed[i+1]

            if prev == 0 and curr == 0 and next == 0:
                flowerbed[i] = 1
                n -= 1
               
            if n == 0:
                return True
                
        if n != 0:
            return False
        