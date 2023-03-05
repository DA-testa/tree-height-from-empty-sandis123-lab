import sys
import threading
import os

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree(parents):
    nodes = [Node(i) for i in range(len(parents))]
    root = None
    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])
    return root

def get_tree_height(root):
    if not root:
        return 0
    height = 0
    for child in root.children:
        height = max(height, get_tree_height(child))
    return height + 1

def read_input():
    input_type = input("Enter input type (F/f for file, K/k for keyboard): ")
    if input_type.lower() == 'f':
        file_name = input("Enter file name: ")
        while 'a' in file_name:
            print("Invalid file name. Please enter a different file name.")
            file_name = input("Enter file name: ")
        file_path = os.path.join(os.getcwd(), 'input', file_name)
        with open(file_path, 'r') as f:
            n = int(f.readline().strip())
            parents = [int(x) for x in f.readline().split()]
    elif input_type.lower() == 'k':
        n = int(input("Enter the number of nodes: "))
        parents = [int(x) for x in input("Enter the parents of each node separated by space: ").split()]
    else:
        print("Invalid input type. Please enter F/f for file or K/k for keyboard.")
        n, parents = None, None
    return n, parents

if __name__ == '__main__':
    n, parents = read_input()
    root = build_tree(parents)
    height = get_tree_height(root)
    print("Height of the tree:", height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
