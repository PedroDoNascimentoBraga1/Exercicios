# inconpleta 


from typing import List

class Solution:
    def maxArea(self, heigth: List[int]) -> int:
        maior = 0
        for i in range(len(heigth)):
            for n in range(len(heigth)):

                if heigth[i] <= heigth[n] and (i - n * heigth[i] > maior) if (i - n >= 0) else (n  - i * heigth[i] > maior):

                    maior = (i - n) * heigth[i] if i - n >= 0 else (n  - i) * heigth[i]

        return 

resposta = Solution()
print(resposta.maxArea([1,1]))