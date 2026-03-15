class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        romandict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        for i in range(len(s)):
            if i < len(s) - 1 and romandict[s[i]] < romandict[s[i+1]]:
                result += (-1) * romandict[s[i]]
            else:
                result += romandict[s[i]]
        return result