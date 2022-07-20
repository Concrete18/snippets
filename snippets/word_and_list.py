def word_and_list(str_list) -> str:
    """
    Converts a string into a comma seperated string of words
    with "and" instead of a comma between the last two entries.
    """
    length = len(str_list)
    if length == 1:
        return str_list[0]
    elif length == 2:
        return f"{str_list[0]} and {str_list[1]}"
    final_string = ""
    for i, entry in enumerate(str_list):
        # first entry
        if i == 0:
            final_string += entry
            continue
        # last entry
        elif i == length - 1:
            final_string += f" and {entry}"
            return final_string
        # middle entries
        else:
            final_string += f", {entry}"
