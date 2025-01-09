class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, value1 in enumerate(nums):
            index2 = index1 + 1
            while index2 < len(nums):
                if value1 + nums[index2] == target:
                    return [index1, index2]
                index2 += 1
        return none
