class Huffman:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None


def huffman_tree_generator(info):
    counter = {}
    for i in info:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    nodes = [Huffman(symbol, frequency) for symbol, frequency in counter.items()]
    print(counter)
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.frequency)

        left_node = nodes.pop(0)
        right_node = nodes.pop(0)

        merged_node = Huffman(None, left_node.frequency + right_node.frequency)
        merged_node.left = left_node
        merged_node.right = right_node
        nodes.append(merged_node)

    return nodes[0]


def build_huffman_code(node, current_code, huffman_codes):
    if node is None:
        return

    if node.symbol is not None:
        huffman_codes[node.symbol] = current_code

    build_huffman_code(node.left, current_code + '0', huffman_codes)
    build_huffman_code(node.right, current_code + '1', huffman_codes)


def huffman_encoding(info):
    if len(info) == 0:
        return None, None

    root = huffman_tree_generator(info)

    huffman_codes = {}
    build_huffman_code(root, "", huffman_codes)

    encoded_element = "".join(huffman_codes[symbol] for symbol in info)

    return encoded_element, root


def huffman_decoding(encoded_element, node):
    if encoded_element is None or node is None:
        return None

    decoded_element = ""
    current_node = node
    for bit in encoded_element:
        if bit == "0":
            current_node = current_node.left

        elif bit == "1":
            current_node = current_node.right

        if current_node.symbol is not None:
            decoded_element += current_node.symbol
            current_node = node
    return decoded_element


data = "this is an example for huffman encoding"

# Encoding
encoded_data, huffman_tree = huffman_encoding(data)
print("Encoded Data:", encoded_data)

# Decoding

decoded_data = huffman_decoding('010101111111000101101', huffman_tree)
print("Decoded Data:", decoded_data)