def decode_huffman(encode, root):
    result = ""
    current = root

    for bit in encode:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.symbol != "*":
            result += current.symbol
            current = root
    return result

