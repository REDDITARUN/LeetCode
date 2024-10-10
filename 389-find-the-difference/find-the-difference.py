class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        dic = {}

        for char in t:
            dic[char] = dic.get(char, 0) + 1

        for char in s:
            dic[char] -= 1

        for char in dic:
            if dic[char] == 1:
                return char