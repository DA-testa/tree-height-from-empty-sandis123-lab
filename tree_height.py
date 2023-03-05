#python3
import sys
import threading
import numpy

def compute_depth(node, children):
    if not children[node]:
        return 1
    max_depth = 0
    for child in children[node]:
        depth = compute_depth(child, children)
        max_depth = max(max_depth, depth)
    return max_depth + 1

def compute_height(n, parents):
    children = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            children[parent].append(i)
    return compute_depth(root, children)

def main():
    input_type = input()
    if 'I' in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)
        print(height)
    elif 'F' in input_type:
        filename = input()
        with open("test/" +filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            height = compute_height(n,parents)
            print(height)
    else:
        print("error")
        exit()

sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
