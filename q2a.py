# Node of a Huffman Tree
import sys


class Nodes:
    def __init__(self, probability, symbol, left=None, right=None):
        # probability of the symbol
        self.probability = probability

        # the symbol
        self.symbol = symbol

        # the left node
        self.left = left

        # the right node
        self.right = right

        # the tree direction (0 or 1)
        self.code = ''

def CalculateProbability(the_data):
    the_symbols = dict()
    for item in the_data:
        if the_symbols.get(item) == None:
            the_symbols[item] = 1
        else:
            the_symbols[item] += 1
    return the_symbols

the_codes = dict()


def CalculateCodes(node, value=''):
    newValue = value + str(node.code)

    if (node.left):
        CalculateCodes(node.left, newValue)
    if (node.right):
        CalculateCodes(node.right, newValue)

    if (not node.left and not node.right):
        the_codes[node.symbol] = newValue

    return the_codes


def HuffmanEncoding(the_data):
    symbolWithProbs = CalculateProbability(the_data)
    the_symbols = symbolWithProbs.keys()

    the_nodes = []

    for symbol in the_symbols:
        the_nodes.append(Nodes(symbolWithProbs.get(symbol), symbol))

    while len(the_nodes) > 1:
        the_nodes = sorted(the_nodes, key=lambda x: x.probability)

        right = the_nodes[0]
        left = the_nodes[1]

        left.code = 0
        right.code = 1

        newNode = Nodes(left.probability + right.probability, left.symbol + right.symbol, left, right)

        the_nodes.remove(left)
        the_nodes.remove(right)
        the_nodes.append(newNode)

    huffmanEncoding = CalculateCodes(the_nodes[0])
    return huffmanEncoding

def main(lines):
    huffmanMap = HuffmanEncoding(lines)

    result = ''
    for x in range(0, 10):
        if str(x) in huffmanMap:
            value = huffmanMap[str(x)] if len(huffmanMap[str(x).strip()]) > 0 else "0"
            result = (str(x) + " " + value + "\n")
        else:
            result = (str(x) + " null" + "\n")
    sys.stdout = result


# the_data = "AAAAAAABBCCCCCCDDDEEEEEEEEE"
the_data = "1751709618360459813571045"
# the_data = "555"
main(the_data)