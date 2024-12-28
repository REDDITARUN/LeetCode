class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        
        short_str = min(strs, key = len)
        
        for i, char in enumerate(short_str):
            for other in strs:
                if i>= len(other) or other[i] != char:
                    return short_str[:i]
        return short_str
        
        
#         prefix = strs[0]
        
        
#         for s in strs[1:]:
            
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]
                
#                 if not prefix:
#                     return ""
            
#         return prefix

#         min_len = min(len(s) for s in strs)

        
#         prefix = ""

       
#         for i in range(min_len):
        
#             current_char = strs[0][i]
#             if all(s[i] == current_char for s in strs):
#                 prefix += current_char
#             else:
#                 break

#         return prefix
        
        