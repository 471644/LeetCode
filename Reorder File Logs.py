You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

Constraints:

1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.

##################################################################################
##################### My Solution ################################################
#################### Fails one test case #########################################
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = list(filter(lambda val:  not val.split()[1].isnumeric() , logs))
        has={}
        for i,val in enumerate(letter_logs):
            has[val[val.find(" ")+1:]]=i
        
        return [letter_logs[i] for i in list(OrderedDict(sorted(has.items())).values())]+list(filter(lambda val: val.split()[1].isnumeric() , logs))


##################################################################################
##################################################################################
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)
        
        
##################################################################################
####################### Best Solution ############################################
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLog=[]
        digitLog=[]
        for l in logs:
            if l.split()[1:][0].isalpha():
                letterLog.append(l)
            else:
                digitLog.append(l)

        letterLog=sorted(letterLog,key=lambda x:[x.split()[1:],x.split()[0]])
        return letterLog+digitLog