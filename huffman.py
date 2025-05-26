import heapq

class Node:
    def _init_(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def _lt_(self, other):
        return self.freq < other.freq

def huffman_coding(freq_map):
    heap = []
    for char in freq_map:
        heapq.heappush(heap, Node(char, freq_map[char]))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    def generate_codes(root, code, codes):
        if root:
            if root.char is not None:
                codes[root.char] = code
            generate_codes(root.left, code + "0", codes)
            generate_codes(root.right, code + "1", codes)

    root = heapq.heappop(heap)
    codes = {}
    generate_codes(root, "", codes)
    return codes

n = int(input("Enter number of characters: "))
freq_map = {}
for _ in range(n):
    char, freq = input("Enter char and freq: ").split()
    freq_map[char] = int(freq)

codes = huffman_coding(freq_map)
print("Huffman Codes:")
for c in codes:
    print(c, ":", codes[c])
