A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:

The first word in the sequence is beginWord.
The last word in the sequence is endWord.
Only one letter is different between each adjacent pair of words in the sequence.
Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with 5 words.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no possible transformation.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the strings in wordList are unique.
######################################################
######################################################

class Solution:
    def preProcess(self,wordList):
        dic = {}
        for word in wordList:
            for c in range(len(word)):
                wildCard = word[:c]+'*'+word[c+1:]
                if wildCard not in dic:
                    dic[wildCard]=[]
                dic[wildCard].append(word)
        return dic
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        preProcessedWords = self.preProcess(wordList)
        queue = deque()
        queue.append([beginWord,1])
        visited = set()
        while queue:
            curr,level = queue.popleft()
            for c in range(len(curr)):
                wildCard = curr[:c]+'*'+curr[c+1:]
                if wildCard in preProcessedWords:
                    for word in preProcessedWords[wildCard]:
                        if word == endWord:
                            return level+1
                        if word not in visited:
                            visited.add(word)
                            queue.append([word,level+1])
        return 0