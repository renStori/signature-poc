def from_coords_to_int(coordinates: list):
    return int("111" + "".join([f"{x:03}{y:03}" for (x, y) in coordinates]))


def from_int_to_coords(big_number):
    string = str(big_number)
    if string.startswith("111"):
        string = string[3:]
    chunks = [string[i : i + 6] for i in range(0, len(string), 6)]
    return [(int(chunk[:3]), int(chunk[3:])) for chunk in chunks]
