class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        get_dict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in get_dict:
                get_dict[sorted_word] = []

            get_dict[sorted_word].append(word)

        return list(get_dict.values())


        