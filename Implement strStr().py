Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
 

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.

########################################################################
################## My Data Science Solution ############################

import numpy as np
class Solution:
    
    
    def strStr(self, haystack: str, needle: str) -> int:
        def similarity(a,b):
            return int(np.linalg.norm(np.array(a) - np.array(b)))
        if (haystack==needle) | (len(needle) ==0):
            return 0
        if (len(haystack) == 0):        
            return -1
                
        needle_=[]
        haystack_=[]
        i=0
        while i<len(haystack):
            if i < len(needle):
                needle_.append(ord(needle[i]))
                haystack_.append(ord(haystack[i]))
                i+=1
            else:
                haystack_.append(ord(haystack[i]))
                i+=1
        
        for j in range((len(haystack)-len(needle))+1):
            if similarity(needle_,haystack_[j:(j+len(needle))]) == 0:
                return j
                    
        return -1




########################################################################
################## Efficient Solution ##################################

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1
        if not haystack:
            if not needle:
                return 0
            else:
                return ans
        
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        
        
        
        
        
        return -1 