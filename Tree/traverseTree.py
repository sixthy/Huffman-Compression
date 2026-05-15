from Huffman.huffmanTree import build_huffman_tree

def traverse_tree(node, code, code_table):
    if node is None:
        return
    if node.symbol != "*":
        code_table[node.symbol] = code
    
    traverse_tree(node.left, code + "0", code_table)
    traverse_tree(node.right, code + "1", code_table)

