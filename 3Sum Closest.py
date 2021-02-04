Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4


############################################
################# My Solution ##############

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sum_min = 999999
        nums.sort()        
        for idx,val in enumerate(nums[:-2]):
            pointer_1 = idx+1
            pointer_2 = len(nums)-1
            while pointer_1 < pointer_2:
                if abs(target-(nums[idx]+nums[pointer_1]+nums[pointer_2])) < abs(target-sum_min):
                    sum_min=nums[idx]+nums[pointer_1]+nums[pointer_2]
                
                elif (nums[idx]+nums[pointer_1]+nums[pointer_2]) > target:
                    pointer_2-=1
                else:
                    pointer_1+=1
        
        return sum_min