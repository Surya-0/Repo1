# huffman code

class Huffman:
    def __init__(self,frequency,symbol):
        self.frequency = frequency
        self.symbol = symbol
        self.left = None
        self.right = None

def build_huffman_tree(info):
    counter = {}
    for symbol in info:
        if symbol not in counter:
            counter[symbol] = 1
        else:
            counter[symbol] += 1
    nodes = [Huffman(frequency,symbol) for symbol,frequency in counter.items()]
    print(counter)
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.frequency)
        left_node = nodes.pop()
        right_node = nodes.pop()
        new_node = Huffman(left_node.frequency+right_node.frequency,None)
        nodes.append(new_node)
    return nodes[0]

def generate_huffman_code(node,current_code,huffman_code):



def huffman_tree_encoding(info):
    if len(info) == 0:
        return None,None
    root = build_huffman_tree(info)
    code = ""
    huffman_code_dict = {}

def huffman_tree_decoding():


if __name__ == '__main__':
    data = "Hello world"
    encoded_data,node = huffman_tree_encoding(data)
