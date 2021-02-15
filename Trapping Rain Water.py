Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
#####################################################
######### My Solution beats 97.82% memory usage #####
#####################################################
class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped_so_far = 0
        for i in range(1,len(height)-1):
            k=(min(max(height[:i]),max(height[i+1:]))-height[i])
            k= k if  k > 0 else 0
            water_trapped_so_far = water_trapped_so_far + k
        return water_trapped_so_far

#####################################################
#####################################################
def findWater(arr, n):
 
    # initialize output
    result = 0
      
    # maximum element on left and right
    left_max = 0
    right_max = 0
      
    # indices to traverse the array
    lo = 0
    hi = n-1
      
    while(lo <= hi): 
     
        if(arr[lo] < arr[hi]):
         
            if(arr[lo] > left_max):
 
                # update max in left
                left_max = arr[lo]
            else:
 
                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo+= 1
         
        else:
         
            if(arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi-= 1
         
    return result
  
# Driver program
 
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
 
print("Maximum water that can be accumulated is ",
        findWater(arr, n))
 
# This code is contributed
# by Anant Agarwal.        