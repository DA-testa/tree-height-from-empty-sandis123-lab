import sys
import threading
import os

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

def main():
    # Get input from user
    file_name = input("Enter file name: ")
    while file_name.lower() == "" or "a" in file_name.lower():
        file_name = input("Enter valid file name: ")

    file_path = os.path.join("folder", file_name)
    if not os.path.exists(file_path):
        print("Error: file not found.")
        return

    with open(file_path) as f:
        input_lines = f.readlines()

    n = int(input_lines[0])
    parents = list(map(int, input_lines[1].strip().split()))

    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

threading.Thread(target=main).start()
