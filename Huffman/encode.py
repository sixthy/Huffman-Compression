def encode(input_str, code_table):
    encoded = ""
    for c in input_str:
        encoded += code_table[c]
    return encoded