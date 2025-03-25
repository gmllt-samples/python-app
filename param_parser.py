import random
import re

def parse_param(input_str, typ="int", default=None):
    items = input_str.split(",")
    values = []

    for item in items:
        if "-" in item:
            start, end = map(lambda x: convert(x.strip(), typ), item.split("-"))
            values.extend(range(int(start), int(end) + 1))
        else:
            values.append(convert(item.strip(), typ))

    return random.choice(values) if values else default

def convert(val, typ):
    val = val.upper()
    match = re.match(r"([\d.]+)([KMG]?)", val)
    if not match:
        return 0

    num = float(match.group(1))
    unit = match.group(2)

    mult = {"": 1, "K": 1024, "M": 1024**2, "G": 1024**3}.get(unit, 1)
    result = num * mult

    return float(result) if typ == "float" else int(result)
