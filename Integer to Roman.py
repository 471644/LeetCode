Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Example 2:

Input: num = 4
Output: "IV"
Example 3:

Input: num = 9
Output: "IX"
Example 4:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


##################################################
##### My Solution ################################
class Solution:
    def intToRoman(self, num: int) -> str:
        power=0
        roman=''
        has = {1:'I',2:"II",3:"III",4:"IV",5:"V",
               6:'VI',7:"VII",8:"VIII",9:"IX",10:"X",
               40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",
               900:"CM",1000:"M"
              }
        while num!=0:
            digit = int(num%10)
            if (digit in has) & (power==0):
                roman= has[digit]+roman  
                
                num=int(num/10)
                power+=1
            elif power==1:
                if digit*(10**power) in has:
                    roman=has[digit*(10**power)]+roman
                elif digit<4:
                    roman=has[10]*digit+roman
                elif digit>5:
                    roman=has[50]+has[10]*(digit-5)+roman
                
                num=int(num/10)
                power+=1
            elif power==2:
                if digit*(10**power) in has:
                    roman=has[digit*(10**power)]+roman
                elif digit<4:
                    roman=has[100]*digit+roman
                elif digit>5:
                    roman=has[500]+has[100]*(digit-5)+roman
                print(roman)
                num=int(num/10)
                power+=1
            
            else:
                if digit*(10**power) in has:
                    roman=has[digit*(10**power)]+roman
                else:
                    roman=has[1000]*digit+roman
                
                print(roman)
                num=int(num/10)
                power+=1
        return roman
        
        
#######################################################
############### Best Solution #########################
def intToRoman(self, num: int) -> str:
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]