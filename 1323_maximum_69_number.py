class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)
        first_6_idx = num_str.find('6')
        if first_6_idx != -1:
            return int(num_str[0: first_6_idx] + '9' + num_str[first_6_idx + 1:])
        return num
