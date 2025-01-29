from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, rigth = 0, len(nums) - 1

        while left <= rigth:
             middle = (left + rigth) // 2

             if nums[middle] == target:
                 return middle
             
             if nums[middle] > target:
                 rigth = middle - 1
             else:
                 left = middle + 1

        return left