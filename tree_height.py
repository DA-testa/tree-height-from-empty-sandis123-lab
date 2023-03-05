import sys
import threading
import os

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

def build_tree(parents):
    nodes = [Node(i) for i in range(len(parents))]
    root = None

    for i in range(len(parents)):
        if parents[i] == -1:
            root = nodes[i]
        else:
            nodes[parents[i]].children.append(nodes[i])

    return root

if __name__ == '__main__':
    input_type = input("Enter input type (F/f for file, K/k for keyboard): ")

    if input_type.lower() == 'f':
        filename = input("Enter filename: ")
        with open(filename) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    else:
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parent of each node: ").split()))

    root = build_tree(parents)

    def height(node):
        if node is None:
            return 0

        child_heights = []
        for child in node.children:
            child_heights.append(height(child))

        return 1 + max(child_heights)

    print(height(root))



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
