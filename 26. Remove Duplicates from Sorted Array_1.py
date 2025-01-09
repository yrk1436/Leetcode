from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        hash_dict:dict = {}
        expected = [] 
        for n in nums:
            if n in hash_dict:
                hash_dict[n] += 1
            else:
                hash_dict[n] = 1
                expected.append(n)        
        nums = expected
        return len(expected), expected
    
s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(f'current array with dups {nums}')
count, new_nums = s.removeDuplicates(nums)
print(f'distinct count = {count}')
print(f'new array now {new_nums}')
        