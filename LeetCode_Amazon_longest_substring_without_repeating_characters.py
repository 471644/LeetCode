#Given a string s, find the length of the longest substring without repeating characters.

 

#Example 1:

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:

#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:

#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#Example 4:

#Input: s = ""
#Output: 0
 

#Constraints:

#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        has={}
        length=0
        length_0=0
        i=0
        if s== "":
            return 0
        if (s== " ") | (len(s)==1):
            return 1
        if len(set(list(s)))==len(list(s)):
            return len(s)
        
        while(i<len(s)):
            if s[i] not in has:
                has[s[i]]=i
                length=length+1
                i=i+1
            else:
                length_0 = length if length>= length_0 else length_0 
                length=0
                i=has[s[i]]+1
                has={}
        return length if length>= length_0 else length_0
         
    
    