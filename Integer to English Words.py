Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

Constraints:

0 <= num <= 231 - 1
   Hide Hint #1  
Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
   Hide Hint #2  
Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
   Hide Hint #3  
There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)

###################################################################
###################################################################

class Solution(object):
    def numberToWords(self, num):
        
        if not num: return 'Zero'
        
        singles = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten',
                  11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen',
                  18:'Eighteen', 19:'Nineteen'}
        
        tens = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
        
        mags = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', \
		'Quintrillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion', 'Decillion']
        
        def num2word(num):
            hun, ten = num // 100, num % 100
            word = []
            
            if hun:
                word.append(singles[hun])
                word.append('Hundred')
            
            if ten in singles:
                word.append(singles[ten])
            else:
                t, s = ten // 10, ten % 10
                
                if t in tens:
                    word.append(tens[t])
                if s in singles:
                    word.append(singles[s])
                
            return ' '.join(word)
        
        result = []
        i = 0
        while num:
            part = num % 1000
            num = num // 1000
            
            if part and i:
                result.append(mags[i])
            
            part = num2word(part)
            if part:
                result.append(part)
                
            i += 1
            
        return ' '.join(reversed(result))