class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)

        if s_len in [0, 1]:
            return s_len

        if len(set(s)) == s_len:
            return s_len

        sub_len = 2
        idx = 0
        end_idx = sub_len
        longest = 1

        times = 1
        while idx < s_len:
            print(times)
            times += 1
            sub = s[idx: end_idx]

            # Has only unique characters
            if len(set(sub)) == sub_len:
                longest = sub_len
                sub_len += 1
            else:
                idx += 1

            end_idx = idx + sub_len

            # Reached the end of the string
            if end_idx > s_len:
                end_idx = idx + sub_len

            # It is no longer possible to have substrings longer than the current longest
            if s_len - idx <= longest:
                return longest

        return longest
