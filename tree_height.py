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
    source = input("Enter input type (I for keyboard input, F for file input): ")
    while source.upper() not in ['I', 'F']:
        source = input("Enter a valid input type (I for keyboard input, F for file input): ")
    if source.upper() == 'I':
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parents of each node (space-separated): ").split()))
        return n, parents
    elif source.upper() == 'F':
        while True:
            file_name = input("Enter the file name: ")
            if "a" in file_name.lower():
                print("File name cannot contain the letter 'a'.")
            else:
                break
        try:
            with open(os.path.join("folder", file_name)) as f:
                input_lines = f.readlines()
        except FileNotFoundError:
            print("Error: file not found.")
            return None, None
        n = int(input_lines[0])
        parents = list(map(int, input_lines[1].strip().split()))
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
