Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

####################################################
############## My Solution #########################

import ast
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        has={}
        nums.sort()
        if len(nums)<3:
            return []
        for i in range((len(nums)-1)):
            s = set()
            current_sum = -nums[i]
            for j in range(i+1,(len(nums))):
                
                    if (current_sum-nums[j]) in s:
                        
                        has[str(sorted([nums[i],nums[j],current_sum-nums[j]]))]=1
                    s.add(nums[j])    
        
        return sorted([ast.literal_eval(x) for x in has.keys()])


####################################################
########## Best Solution ###########################

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=  set()
        seen = {}
        for i, val1 in enumerate(nums):
            # if val1 not in dups:
            #     dups.add(val1)
            for j, val2 in enumerate(nums[i+1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i
        return sorted(res)