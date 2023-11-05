import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(char_freq):
    heap = [HuffmanNode(symbol, freq) for symbol, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node.symbol:
        huffman_codes[node.symbol] = current_code
    if node.left:
        build_huffman_codes(node.left, current_code + '0', huffman_codes)
    if node.right:
        build_huffman_codes(node.right, current_code + '1', huffman_codes)

if __name__ == "__main__":
    num_chars = int(input("Enter the number of characters: "))
    chars = []
    freq = []

    for i in range(num_chars):
        char = input(f"Enter character {i + 1}: ")
        frequency = int(input(f"Enter frequency for character {char}: "))
        chars.append(char)
        freq.append(frequency)

    char_freq = dict(zip(chars, freq))
    root = build_huffman_tree(char_freq)
    huffman_codes = {}
    build_huffman_codes(root, '', huffman_codes)

    print(f"Characters: {chars}")
    print(f"Frequency: {freq}")
    print("Huffman Encoding:")
    for char, code in huffman_codes.items():
        print(f"{char} -> {code}")
