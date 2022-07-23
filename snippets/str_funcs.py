import re


class str_funcs:
    def url_sanitize(self, string, space_replace="-"):
        """
        Removes all illegal URL characters from the given `string`.

        Replaces all spaces with the `space_replace`.
        """
        string = string.replace(" ", space_replace)
        # Allowed characters (0-9, A-Z, a-z, "-", ".", "_", "~")
        string = re.sub(r"[^a-zA-Z0-9-._~]+", "", string).strip()
        while "--" in string:
            string = string.replace("--", "-")
        return string

    def unicode_remover(self, string) -> str:
        """
        Removes unicode from `string`.
        """
        if type(string) != str:
            return string
        replace_dict = {
            "\u2122": "",  # Trademarked sign
            "\u00ae": "",  # REGISTERED SIGN
            "\u00ae": "",  # REGISTERED SIGN
            "\u00e5": "a",  # a
            "\u00f6": "o",  # LATIN SMALL LETTER O WITH DIAERESIS
            "\u00e9": "e",  # LATIN SMALL LETTER E WITH ACUTE
            "\u2013": "-",  # EN DASH
            "&amp": "&",  # &
        }
        for unicode in replace_dict.keys():
            if unicode in string:
                for unicode, sub in replace_dict.items():
                    string = string.replace(unicode, sub)
                break
        conv_string = string.encode("ascii", "ignore").decode()
        return conv_string.strip()

    def word_and_list(self, str_list) -> str:
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

    def list_in_string(self, list: list, string: str, lowercase: bool = True):
        """
        Returns True if any entry in the given `list` is in the given `string`.

        Setting `lowercase` to True allows you to make the check
        set all to lowercase.
        """
        if lowercase:
            return any(x.lower() in string.lower() for x in list)
        else:
            return any(x in string for x in list)
