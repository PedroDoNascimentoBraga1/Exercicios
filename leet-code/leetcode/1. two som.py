from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            par = target - nums[i]
            if par in nums and nums.index(par) != i:
                return ( i,nums.index(par))
            
resposta = Solution()
print(resposta.twoSum([3,3],6))