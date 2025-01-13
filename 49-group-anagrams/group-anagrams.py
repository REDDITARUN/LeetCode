class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        stored = {}
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in stored:
                stored[sorted_word] = []
            stored[sorted_word].append(word)

        return list(stored.values())


        