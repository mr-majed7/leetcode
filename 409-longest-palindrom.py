class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = {}
        for c in s:
            if c not in frequency:
                frequency[c] = 1
            else:
                frequency[c] +=1
        length = 0
        for count in frequency.values():
            length += count//2 * 2
            if length%2 == 0 and count %2 == 1:
                length +=1
        return length