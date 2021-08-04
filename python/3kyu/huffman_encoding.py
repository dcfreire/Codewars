# %%
import collections
from queue import PriorityQueue
from functools import total_ordering
# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)

# %%


@total_ordering
class Node():
    def __init__(self, weight):
        self.weight = weight
        self.right = None
        self.left = None
        self.letter = None

    def __eq__(self, value):
        return self.weight == value

    def __gt__(self, value):
        return self.weight > value


class LeafNode(Node):
    def __init__(self, weight, letter):
        super().__init__(weight)
        self.letter = letter


class InternalNode(Node):
    def __init__(self, children):
        super().__init__(children[0].weight + children[1].weight)
        self.right = children[0]
        self.left = children[1]


def frequencies(s):
    return [(x, y) for x, y in collections.Counter(s).items()]

# takes: [ (str, int) ], str; returns: String (with "0" and "1")


codes = {}


def get_codes(tree, curcode=""):
    global codes
    if tree is not None:
        if tree.left:
            get_codes(tree.left, curcode + "0")
        if tree.right:
            get_codes(tree.right, curcode + "1")
        if tree.letter:
            codes[tree.letter] = curcode


def get_tree(freqs):
    qu = PriorityQueue()
    for letter, weight in freqs:
        qu.put(LeafNode(weight, letter))
    while qu.qsize() > 1:
        nn = InternalNode((qu.get(), qu.get()))
        qu.put(nn)
    return nn


def encode(freqs, s):
    if len(freqs) <= 1:
        return None
    if len(s) == 0:
        return ''
    codes.clear()
    get_codes(get_tree(freqs))
    return ''.join([codes[c] for c in s])

# takes [ [str, int] ], str (with "0" and "1"); returns: str


def decode(freqs, bits):
    if len(freqs) <= 1:
        return None
    if len(bits) == 0:
        return ''
    codes.clear()
    get_codes(get_tree(freqs))
    inv_map = {v: k for k, v in codes.items()}
    return re.compile('|'.join(inv_map.keys())).sub(lambda x: inv_map[x.group()], bits)
