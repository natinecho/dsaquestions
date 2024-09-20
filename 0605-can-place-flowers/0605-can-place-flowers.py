class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        nn = 0

        for i in range(len(flowerbed)):
            if i == 0 and  flowerbed[0] == 0 and flowerbed[i + 1] == 0:
                flowerbed[0] =  1
                nn +=1

            elif i < len(flowerbed) -1 and flowerbed[i] == flowerbed[i + 1] ==  flowerbed[i - 1] == 0:               
                flowerbed[i] = 1
                nn += 1

            elif i == len(flowerbed) - 1 and  flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                nn += 1
                flowerbed[i] += 1  

        return nn >= n