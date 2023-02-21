import sys
import threading
import os

if not os.path.exists("folder"):
    os.makedirs("folder")

class Node:
    def __init__(self, parent=None):
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def compute_height(n, parents):
    nodes = [Node() for _ in range(n)]
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = nodes[i]
        else:
            nodes[parents[i]].add_child(nodes[i])

    def get_height(node):
        if not node.children:
            return 1
        else:
            return 1 + max(get_height(child) for child in node.children)

    return get_height(root)

def get_input():
    source = input("Enter a valid input type (I for keyboard input, F for file input): ")
    n = None
    parents = None

    if source == 'I':
        n = int(input())
        parents = list(map(int, input().split()))
    elif source == 'F':
        filename = input("Enter the input file name: ")
        try:
            with open(filename, 'r') as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except EOFError:
            pass

    return n, parents

def main():
    n, parents = get_input()
    if not parents:
        return

    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
