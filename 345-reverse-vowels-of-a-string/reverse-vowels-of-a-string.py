class Solution:
    def reverseVowels(self, s: str) -> str:
        l = len(s)
        s = list(s)
        p1 = 0
        p2 = l - 1

        vov = set('aeiouAEIOU')

        while p1 < p2:
            if s[p1] not in vov:
                p1 += 1
                continue
            if s[p2] not in vov:
                p2 -= 1
                continue
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1

        return ''.join(s)


        