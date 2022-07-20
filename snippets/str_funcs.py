import re


def url_sanitize(string, space_replace="-"):
    """
    Removes all illegal URL characters from the given `string`.

    Turns spaces into dashes if `space_to_dash` is true.
    """
    string = string.replace(" ", space_replace)
    # Allowed characters (0-9, A-Z, a-z, "-", ".", "_", "~")
    string = re.sub(r"[^a-z0-9-._~]+", "", string.lower()).strip()
    while "--" in string:
        string = string.replace("--", "-")
    return string


def unicode_remover(string) -> str:
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
