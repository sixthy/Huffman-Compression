from Node.node import Node
from Huffman.encode import encode
from Huffman.huffmanTree import build_huffman_tree 
from Tree.bodyTree import build_code_table, build_frequency_table, bit_string_to_bytes, bytes_to_bit_string
from Huffman.decodeHuffman import decode_huffman

def main():
    base = "Input/Text5.txt"
    out = "Compressed_Files/Text5_encoded.bin"
    outD= "Decompressed_Files/Text5_decoded.txt"

    with open(base, "r", encoding="utf-8") as f:
        input_str = f.read()
    
    print("====================================================================================================================================================")

    print("Input length:", len(input_str))
    print("\nInput start:", repr(input_str[:50]))
    
    frequency_table = build_frequency_table(input_str)
    print("\nFrequency table keys:", list(frequency_table.keys())[:1000])
    
    root = build_huffman_tree(frequency_table)
    print("\nRoot symbol:", root.symbol if root else None)
    
    code_table = build_code_table(root)
    print("\nCode table keys:", list(code_table.keys())[:1000])

    print("====================================================================================================================================================")
    
    encoded = encode(input_str, code_table)
    print("\nEncoded length:", len(encoded))
    print("\nEncoded start:", encoded[:1000])

    byte_data, padding = bit_string_to_bytes(encoded)
    with open(out, "wb") as f:
        f.write(bytes([padding]))  
        f.write(byte_data)
    print("\nEncoded binary saved to", out)

    print("====================================================================================================================================================")

    with open(out, "rb") as f:
        padding_read = f.read(1)[0]
        byte_data_read = f.read()
    
    bit_string = bytes_to_bit_string(byte_data_read, padding_read)
    decoded = decode_huffman(bit_string, root)
    print("\nDecoded lenght:", len(decoded))
    print("\nDecoded start:", decoded[:1000])

    print("====================================================================================================================================================")
    
    with open(outD, "w", encoding="utf-8") as f:
        f.write(decoded)
    print("\nDecoded string saved to", outD)


if __name__ == "__main__":
    main()

