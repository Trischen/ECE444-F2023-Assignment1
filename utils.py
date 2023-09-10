class utils:
    def reversed(num):
        if not isinstance(num, int):
            return "Invalid datatype"
        num_to_str = str(num)
        rev_str = num_to_str[::-1]
        str_to_num = int(rev_str)
        return str_to_num
    def formatter(num):
        if not isinstance(num, int):
            return "Invalid datatype", None
        bin_num = bin(num)
        oct_num = oct(num)
        return bin_num, oct_num