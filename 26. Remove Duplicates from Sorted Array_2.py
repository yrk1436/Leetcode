from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1

        print(f'new array now {nums}')
        return l

    
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(f'current array with dups {nums}')
count = s.removeDuplicates(nums)
print(f'distinct count = {count}')

        