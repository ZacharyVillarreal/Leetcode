class Solution:
    def maximum69Number (self, num: int) -> int:
        max_num = num
        lst_num = list(str(num))
        for i in range(len(lst_num)):
            if lst_num[i] == "6":
                lst_num[i] = "9"
                if int("".join(lst_num)) > max_num:
                    max_num = int("".join(lst_num))
                lst_num[i] = "6"
            else:
                lst_num[i] = "6"
                if int("".join(lst_num)) > max_num:
                    max_num = int("".join(lst_num))
                lst_num[i] = "9"
        return int(max_num)
