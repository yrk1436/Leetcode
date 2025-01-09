from typing import List, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        prev:dict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]            
            prev[n] = i
        return None
