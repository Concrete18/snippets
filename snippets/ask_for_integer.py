def ask_for_integer(msg=None, num_range=False, allow_blank=False) -> int or bool:
    """
    Asks for a integer until an integer is given.
    """
    if msg is None:
        msg = "Type a Number: "
    num = input(msg)
    if allow_blank and num == "":
        return ""
    if num_range:
        min = num_range[0]
        max = num_range[1]
        while True:
            if num.isdigit():
                if min <= int(num) <= max:
                    break
            num = input(msg)
            if allow_blank and num == "":
                return ""
    else:
        while not num.isdigit():
            num = input(msg)
            if allow_blank and num == "":
                return ""
    return int(num)
