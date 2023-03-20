class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if not flowerbed[i]:
                if (not i or not flowerbed[i-1]):
                    if (i == len(flowerbed)-1 or not flowerbed[i+1]):
                        flowerbed[i] = 1
                        count += 1
                        
            if count >= n:
                return True
            i += 1
            
        return False