class Huffman:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None


def build_huffman_tree(info):
    counter = {}
    for symbol in info:
        if symbol in counter:
            counter[symbol] += 1
        else:
            counter[symbol] = 1
    node_list = [Huffman(symbol, frequency) for symbol, frequency in counter.items()]
    while len(node_list) > 1:
        node_list.sort(key=lambda x: x.frequency)
        left_node = node_list.pop()
        right_node = node_list.pop()
        new_node = Huffman(None, left_node.frequency + right_node.frequency)
        new_node.left = left_node
        new_node.right = right_node
        node_list.append(new_node)
    return node_list[0]


def build_huffman_code(start, code, huffman_code):
    if start is None:
        return
    if start.symbol is not None:
        huffman_code[start.symbol] = code
    build_huffman_code(start.left, code + '0', huffman_code)
    build_huffman_code(start.right, code + '1', huffman_code)


def huffman_encode(info):
    root = build_huffman_tree(info)
    huffman_codes = {}
    code_data = ""
    build_huffman_code(root, code_data, huffman_codes)
    encoded_element = "".join(huffman_codes[symbol] for symbol in info)
    return encoded_element, root


def huffman_decode(info, root):
    if info is None or root is None:
        return None
    decoded_element = ""
    current_node = root
    for bit in info:
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right
        if current_node.symbol is not None:
            decoded_element += current_node.symbol
            current_node = root
    return decoded_element


if __name__ == '__main__':
    data = "Hello world"
    encoded_data, huffman_tree = huffman_encode(data)
    print(encoded_data)
    decoded_data = huffman_decode(encoded_data,huffman_tree)
    print(decoded_data)