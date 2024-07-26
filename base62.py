from string import ascii_uppercase, ascii_lowercase, digits

ALPHANUMERIC = digits + ascii_uppercase + ascii_lowercase  # Base62


def int_to_base62(big_number):
    big_number = int(big_number)
    if big_number == 0:
        return ALPHANUMERIC[0]
    encoded = []
    base = len(ALPHANUMERIC)
    while big_number > 0:
        big_number, remainder = divmod(big_number, base)
        encoded.append(ALPHANUMERIC[remainder])
    encoded.reverse()
    return "".join(encoded)


def base62_to_int(base62_string):
    base = len(ALPHANUMERIC)
    num = 0
    for char in base62_string:
        num = num * base + ALPHANUMERIC.index(char)
    return num
