from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for n in nums:
            if n != val:
                nums[l] = n
                l += 1
        
        return l



s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(f'current array with dups {nums}')
count = s.removeElement(nums, 1)
print(f'distinct count = {count}')