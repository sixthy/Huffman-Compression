from Tree.traverseTree import traverse_tree

def build_frequency_table(input_str):
    frequency_table = {}
    for c in input_str:
        frequency_table[c] = frequency_table.get(c, 0) + 1
    return frequency_table

def build_code_table(root):
    code_table = {}
    traverse_tree(root, "", code_table)
    return code_table

def bit_string_to_bytes(bit_string):
    padding = (8 - len(bit_string) % 8) % 8
    padded_bits = bit_string + '0' * padding
    
    byte_array = bytearray()
    for i in range(0, len(padded_bits), 8):
        byte = int(padded_bits[i:i+8], 2)
        byte_array.append(byte)
    
    return bytes(byte_array), padding

def bytes_to_bit_string(byte_data, padding):
    
    bit_string = ''
    for byte in byte_data:
        bit_string += format(byte, '08b')
    
    if padding > 0:
        bit_string = bit_string[:-padding]
    
    return bit_string





