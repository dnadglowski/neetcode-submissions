class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        lists = []
        while w1 in range(len(word1)) and w1 in range(len(word2)):
            lists.append(word1[w1])
            lists.append(word2[w1])
            w1+=1

        if len(word1) > len(word2):
            lists.append(word1[w1:])
        elif len(word1) < len(word2):
             lists.append(word2[w1:])


        return(''.join(lists))