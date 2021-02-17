Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
###########################################################
############### My Solution ###############################
###########################################################
### Submission Result: Time Limit Exceeded ################
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [math.prod(nums[:i] + nums[i+1:]) for i in range(len(nums))]
        
        
##########################################################
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_l = list(accumulate(nums[:-1], mul, initial=1))
        prod_r = list(accumulate(nums[1:][::-1], mul, initial=1))[::-1]
        return list(map(mul, prod_l, prod_r))
        
        
##########################################################
######### Lay-man Solution ###############################
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Base case 
        if len(nums) == 1:            
            return 0
        i, temp = 1, 1
        # Allocate memory for the product array  
        prod = [1 for i in range(len(nums))] 
        # Initialize the product array as 1  
        # In this loop, temp variable contains product of 
        # elements on left side excluding arr[i]  
        for i in range(len(nums)): 
            prod[i] = temp 
            temp *= nums[i] 
        # Initialize temp to 1 for product on right side  
        temp = 1
        # In this loop, temp variable contains product of 
        # elements on right side excluding arr[i]  
        for i in range(len(nums) - 1, -1, -1): 
            prod[i] *= temp 
            temp *= nums[i] 
         
        return prod