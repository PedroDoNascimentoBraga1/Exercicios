from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maior = max(candies)
        for i in range(len(candies)):
            candies[i] = True if candies[i] + extraCandies >= maior else False 
        return candies

resultado = Solution()
print(resultado.kidsWithCandies([2,3,5,1,3] , 3))

