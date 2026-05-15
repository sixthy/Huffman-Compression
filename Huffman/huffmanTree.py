from Node.node import Node

def build_huffman_tree(frequency_table):
        nodes = [Node(symbol, frequency) for symbol, frequency in frequency_table.items()]
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.frequency)
            left_node, right_node = nodes[0], nodes[1]
            parent_node = Node("*", left_node.frequency + right_node.frequency)
            parent_node.left = left_node
            parent_node.right = right_node
            nodes = nodes[2:]
            nodes.append(parent_node)
        return nodes[0]