ROMAN_TO_INT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

EDGE_CASES = ["IV", "IX", "XL", "XC", "CD", "CM"]


class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        idx = 0
        s_len = len(s)
        while idx < s_len:
            digit = s[idx]
            if idx < s_len - 1 and f"{digit}{s[idx + 1]}" in EDGE_CASES:
                integer += ROMAN_TO_INT[s[idx + 1]] - ROMAN_TO_INT[digit]
                idx += 2
            else:
                integer += ROMAN_TO_INT[digit]
                idx += 1

        return integer
